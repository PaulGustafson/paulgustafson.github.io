# The Mathematics Physics Demands

This directory is the independent source tree for the physics-organized
companion to `../Coordinate_free_Linear_Algebra.tex`. The original manuscript
is not an input to this build and is not modified by it.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The book has independent chapter, theorem, equation, and exercise numbering.
Editorial transfers between the two books are deliberate and recorded in
`PROVENANCE.md`; there is no synchronization script.

Validated release PDFs are stored separately under `releases/` and named with
the companion manuscript's own version number.

Source layout:

- `main.tex`: book preamble and source order
- `frontmatter/`: independent introduction
- `parts/`: the six physical parts
- `backmatter/`: the book's selected bibliography
- `PROVENANCE.md`: passage-level adaptation ledger
- `CHANGELOG.md`: companion-manuscript version history
- `releases/`: versioned companion-book PDFs
