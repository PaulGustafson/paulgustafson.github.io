#!/usr/bin/env python3
"""Audit the exercise manuscript against its fixed table of contents."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "Mathematics_of_Lattice_Models.tex"


def group(text, start):
    """Read a balanced TeX group and return its contents and next position."""
    assert text[start] == "{"
    depth = 1
    end = start + 1
    while depth and end < len(text):
        if text[end] == "{":
            depth += 1
        elif text[end] == "}":
            depth -= 1
        end += 1
    if depth:
        raise ValueError("Unclosed TeX group")
    return text[start + 1 : end - 1], end


def normalize(title):
    marker = r"\texorpdfstring"
    while marker in title:
        start = title.index(marker)
        tex, end = group(title, start + len(marker))
        _, end = group(title, end)
        title = title[:start] + tex + title[end:]
    title = re.sub(r"\\(?:mathfrak|mathrm|mathbf|mathbb)", "", title)
    title = title.replace(r"\log", "log")
    title = re.sub(r"[$\\{}]", "", title)
    return " ".join(title.replace("--", "–").split())


def audit():
    failures = []
    expected = []
    conventions = (ROOT / "MANUSCRIPT_CONVENTIONS.md").read_text()
    for line in conventions.splitlines():
        if re.match(r"\| [IVX]+\. ", line):
            part, sections = line.strip("|").split("|")
            part = re.sub(r"^\s*[IVX]+\.\s*", "", part)
            expected.append(
                (normalize(part), [normalize(s) for s in sections.split(";")])
            )
    if len(expected) != 12:
        failures.append("The convention table must contain twelve parts.")

    entry = ENTRY.read_text()
    inputs = re.findall(r"\\input\{([^}]+)\}", entry)
    wanted_inputs = [f"Lattice_Models_P{i:02}" for i in range(1, 13)]
    if inputs != wanted_inputs:
        failures.append("Entry-point inputs differ from the twelve-part order.")
    if r"\title{Mathematics via Lattice Models}" not in entry:
        failures.append("The manuscript title does not match the requested title.")
    bibkeys = re.findall(r"\\bibitem\{([^}]+)\}", entry)
    if len(set(bibkeys)) != len(bibkeys):
        failures.append("Duplicate bibliography keys.")
    citations = set()
    exercise_count = section_count = 0

    for index, stem in enumerate(wanted_inputs):
        path = ROOT / f"{stem}.tex"
        if not path.exists():
            failures.append(f"{path.name}: missing part file")
            continue
        source = path.read_text()
        source = re.sub(r"(?<!\\)%[^\n]*", "", source)
        parts, sections = [], []
        for match in re.finditer(r"\\(part|section)\{", source):
            title, _ = group(source, match.end() - 1)
            (parts if match[1] == "part" else sections).append(normalize(title))
        if index < len(expected):
            title, headings = expected[index]
            if parts != [title] or sections != headings:
                failures.append(
                    f"{path.name}: TOC mismatch\n"
                    f"  actual: {parts}, {sections}\n"
                    f"  expected: {[title]}, {headings}"
                )
        section_count += len(sections)
        forbidden = re.search(
            r"\\(?:subsection|subsubsection|paragraph|subparagraph|label|ref|eqref)\b"
            r"|\\begin\{(?:definition|theorem|lemma|proposition|corollary|"
            r"remark|example|proof)\}"
            r"|\b(?:TODO|FIXME|placeholder|dualizable)\b",
            source,
        )
        if forbidden:
            failures.append(f"{path.name}: forbidden structure {forbidden[0]!r}")
        exercises = list(
            re.finditer(
                r"\\begin\{exercise\}\[([^\n]*)\](.*?)\\end\{exercise\}",
                source,
                re.S,
            )
        )
        exercise_count += len(exercises)
        if len(exercises) != source.count(r"\begin{exercise}"):
            failures.append(f"{path.name}: missing title or unbalanced exercises")
        if not exercises or not exercises[-1][1].startswith("Prediction:"):
            failures.append(f"{path.name}: missing final prediction exercise")
        for match in re.finditer("assume, as proved by", source, re.I):
            if not exercises or match.start() < exercises[-1].start():
                failures.append(f"{path.name}: external theorem outside final exercise")
        if re.search(r"take as known|used without proof|is quoted, not derived", source, re.I):
            failures.append(f"{path.name}: unsupported theorem wording")
        body = re.sub(
            r"\\begin\{exercise\}.*?\\end\{exercise\}", "", source, flags=re.S
        )
        for match in reversed(list(re.finditer(r"\\(?:part|section)\{", body))):
            _, end = group(body, match.end() - 1)
            body = body[: match.start()] + body[end:]
        if body.strip():
            failures.append(f"{path.name}: text outside exercises: {body.strip()[:80]!r}")
        # Each prescribed subject must actually contain an exercise.
        for chunk in re.split(r"\\section\{", source)[1:]:
            if r"\begin{exercise}" not in chunk:
                failures.append(f"{path.name}: empty section")
        for keylist in re.findall(r"\\cite\{([^}]+)\}", source):
            citations.update(k.strip() for k in keylist.split(","))

    if citations - set(bibkeys):
        failures.append(f"Missing bibliography keys: {sorted(citations - set(bibkeys))}")
    if set(bibkeys) - citations:
        failures.append(f"Uncited bibliography keys: {sorted(set(bibkeys) - citations)}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(
        f"PASS: 12 parts, {section_count} prescribed sections, "
        f"{exercise_count} titled exercises, 12 final predictions, "
        f"{len(citations)} resolved bibliography entries."
    )
    print("PASS: exercise-only body, fixed TOC, and final-only external hypotheses.")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
