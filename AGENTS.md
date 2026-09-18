# Manuscript style

These rules apply to the manuscript entry point
`Mathematics_of_Lattice_Models.tex` and its part files
`Lattice_Models_P01.tex` through `Lattice_Models_P12.tex` (one file per
part).

- The body should consist of exercises that introduce the required definitions
  and state major results.
- Do not use standalone `definition` environments. Introduce each definition,
  together with its hypotheses, notation, conventions, and defining formulas,
  at the beginning of the first exercise that uses it.
- Put theorem statements and substantial consequences in exercises.
- Title each exercise by the full mathematical subject it introduces and
  develops, not merely by the last lemma or calculation requested.
- Use lettered parts when an exercise has genuinely distinct stages.  Keep a
  single continuous argument unitemized.
- Do not add motivational, transitional, interpretive, or summary prose. In
  particular, omit section introductions and sentences explaining what a
  definition "shows," "means," "records," or "indicates."
- Do not add minor computational drills merely to fill out a section. Keep
  exercises for structurally important results.
- Require each exercise to be solvable from definitions and results developed
  earlier in the manuscript. Do not compress a theorem requiring substantial
  undeveloped machinery into a single instruction to prove it; either build a
  sufficient exercise sequence or restrict the result to a developed model.
- Preserve mathematical qualifications and normalization conventions needed
  for correctness; concision must not remove hypotheses or domain conditions.
- Keep the manuscript coordinate-free in substance, not merely in vocabulary.
  Never introduce an arbitrary auxiliary basis, coordinate system, frame,
  matrix unit, eigenvector family, indexed total family, component expansion,
  or local trivialization to represent an otherwise intrinsic object without
  the user's explicit approval.
- Do not repair a choice-dependent passage by renaming a basis as a complete
  family or by replacing it with finite-spanning or linear-independence
  language. Delete minor passages; state major results through intrinsic
  decompositions, spectral projections, universal properties, categorical
  maps, orbit maps, orthogonality relations, kernels, or transform identities.
- Named special-function systems and distinguished concrete models are allowed
  when they are themselves the mathematical subject rather than an auxiliary
  device. This includes Fourier modes, spherical harmonics, Hermite functions,
  concrete matrix ensembles, configuration-indexed transfer matrices, and
  specified fundamental corepresentations. State their defining structure
  explicitly. If it is unclear whether a presentation is intrinsic content or
  an auxiliary choice, ask the user before retaining it.
- Charts, frame bundles, and local trivializations may appear when they define
  the geometric object itself. Structural choices and normalization data such
  as positive roots, Haar measures, branches, and Frobenius conventions must
  remain explicit when the resulting formulas depend on them.
- Define a finite-dimensional vector space by the existence of evaluation and
  coevaluation maps satisfying the two snake identities. Use the term
  "finite-dimensional" directly; do not introduce the word "dualizable" or
  compare this definition with a coordinate definition.
- Define trace using evaluation, symmetry, and coevaluation, and define the
  determinant through the action on the highest exterior power. Prefer the
  analogous intrinsic formulation for later constructions, including rigid
  duals and Tannaka coproducts.
- For distinguished special-function systems, state orthogonality,
  completeness, kernel, or inversion identities without calling the system a
  basis.

## Model-driven part structure

- Treat each `\part` as one lattice model and each `\section` inside it as
  one mathematical subject that the model forces. The part and section titles
  are the fixed table of contents (see `MANUSCRIPT_CONVENTIONS.md`); do not
  add, remove, rename, or reorder them without the user's instruction.
- Use only `\part` and `\section` headings. Do not add `\subsection`,
  `\subsubsection`, or lower-level divisions. A table-of-contents bullet is a
  syllabus item, not a mandate for a heading of its own below the section.
- Organize every part, through its exercise sequence, into this progression:
  the model (configuration space, weights or Hamiltonian, measure, symmetry);
  the mathematical structures its sections name, each with the identity,
  decomposition, or classification it realizes; a quantitative physical
  prediction. These are roles in the argument, not headings to print.
- Every part must culminate in a substantial exercise that uses the part's
  mathematics to derive a quantitative, experimentally testable prediction:
  a critical temperature or exponent, a residual entropy, a dispersion
  relation, a crossing probability, a degeneracy, a braiding phase, a string
  tension, an edge multiplet, a gap equation. State the model, normalization
  conventions, observable, and prediction in the exercise. When experimental
  evidence is cited, distinguish the derived prediction, modeling
  assumptions, measured quantity, and limitations of the comparison.
- Each notion has one owner section; later sections use it by naming that
  section ("the transfer matrix of the section Transfer matrices"). There are
  no `\label`/`\ref` cross-references.
- A deep external theorem may be adopted as a cited hypothesis only inside a
  part's final prediction exercise, and only with the words "assume, as
  proved by". Elsewhere restrict the claim to what the book has developed.
- Introduce prerequisites before their first use and do not reintroduce them
  in later sections.
- Treat general topology, including compactness, local compactness, Borel
  sets, regular Borel measures, and the spaces $C_b(X)$, $C_0(X)$, and
  $C_c(X)$, as a prerequisite for the course; do not define these notions in
  the manuscript.
- Preserve the exercise-driven format: definitions precede their first use
  within the relevant exercise, and applications and experimental
  interpretations belong in exercises, not in transitional prose.

- After changing the TeX source, rebuild and validate the tracked PDF. Commit
  and push the TeX and PDF together unless the user requests otherwise.
