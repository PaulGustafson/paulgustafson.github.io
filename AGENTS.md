# Manuscript style

These rules apply to `A_Physical_Introduction_to_Higher_Mathematics.tex`.

- The body should consist of definitions and exercises stating major results.
- Put theorem statements and substantial consequences in exercises, not in
  definition environments.
- Definitions should contain only the hypotheses, notation, conventions, and
  formulas needed to define the object.
- Do not add motivational, transitional, interpretive, or summary prose.
  In particular, omit section introductions and sentences explaining what a
  definition "shows," "means," "records," or "indicates."
- Do not add minor computational drills merely to fill out a section. Keep
  exercises for structurally important results.
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
- Define a finite-dimensional linear space by the existence of evaluation and
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
- After changing the TeX source, rebuild and validate the tracked PDF. Commit
  and push the TeX and PDF together unless the user requests otherwise.
