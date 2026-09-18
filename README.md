# paulgustafson.github.io

[Mathematics via Lattice Models](Mathematics_of_Lattice_Models.pdf) is an
exercise-driven manuscript in twelve model-based parts. Its entry point is
`Mathematics_of_Lattice_Models.tex`, with one `Lattice_Models_PNN.tex` file
per part. The `old_*.tex` files preserve material from the previous organization.

The fixed table of contents and editing rules are in
[MANUSCRIPT_CONVENTIONS.md](MANUSCRIPT_CONVENTIONS.md); current coverage
and further development are in [MANUSCRIPT_TODO.md](MANUSCRIPT_TODO.md).

Build and validate the tracked PDF with:

```sh
bash scripts/build_lattice_manuscript.sh
```

This requires Python 3, pdfLaTeX with the packages in the entry point, and
Poppler's `pdftotext` and `pdfinfo`. Build files are kept in a temporary
directory. To run just the source audit:

```sh
python3 scripts/audit_lattice_manuscript.py
```
