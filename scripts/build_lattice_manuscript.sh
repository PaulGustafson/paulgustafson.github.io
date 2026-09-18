#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"
python3 scripts/audit_lattice_manuscript.py

build_dir="$(mktemp -d "${TMPDIR:-/tmp}/lattice-models.XXXXXX")"
trap 'rm -rf "$build_dir"' EXIT
manuscript="Mathematics_of_Lattice_Models"

for pass in 1 2 3; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error \
        -output-directory="$build_dir" "$manuscript.tex" \
        > "$build_dir/pass-$pass.log" 2>&1; then
        cat "$build_dir/pass-$pass.log" >&2
        exit 1
    fi
done

python3 - "$build_dir/$manuscript.log" "$build_dir/$manuscript.toc" <<'PY'
from pathlib import Path
import re
import sys

log, toc = (Path(name).read_text() for name in sys.argv[1:])
errors = re.findall(
    r"^.*(?:Overfull \\[hv]box|Missing character|undefined|"
    r"Rerun to get|Label\(s\) may have changed).*$",
    log,
    re.M,
)
if errors:
    raise SystemExit("\n".join(errors))
for kind, count in (("part", 12), ("section", 64)):
    actual = len(re.findall(r"\\contentsline \{" + kind + r"\}", toc))
    if actual != count:
        raise SystemExit(f"Built TOC has {actual} {kind} entries; expected {count}.")
PY

pdftotext "$build_dir/$manuscript.pdf" "$build_dir/manuscript.txt"
python3 - "$build_dir/manuscript.txt" <<'PY'
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text()
for required in ("Mathematics via Lattice Models", "Geometric Langlands", "References"):
    if required not in text:
        raise SystemExit(f"Missing text in the rendered PDF: {required}")
PY

cp "$build_dir/$manuscript.pdf" "$manuscript.pdf"
pdfinfo "$manuscript.pdf" | sed -n '/^Title:/p; /^Pages:/p'
echo "PASS: three LaTeX passes, stable TOC, resolved citations, no overfull boxes."
