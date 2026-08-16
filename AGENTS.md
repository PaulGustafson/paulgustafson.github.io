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
- Keep the manuscript coordinate-free. Never choose a basis or introduce a
  basis-dependent formula, proof, definition, or exercise without the user's
  explicit approval.
- Do not replace basis language with assertions about finite spanning or
  linear independence. State intrinsic decompositions, universal properties,
  categorical maps, orthogonality relations, completeness statements, or
  transform identities instead.
- Define a finite-dimensional linear space by the existence of evaluation and
  coevaluation maps satisfying the two snake identities. Use the term
  "finite-dimensional" directly; do not introduce the word "dualizable" or
  compare this definition with a coordinate definition.
- Define trace using evaluation, symmetry, and coevaluation, and define the
  determinant through the action on the highest exterior power. Prefer the
  analogous intrinsic formulation for later constructions, including rigid
  duals and Tannaka coproducts.
- For distinguished special-function systems such as Fourier modes, spherical
  harmonics, and Hermite functions, state orthogonality, completeness, kernel,
  or inversion identities without calling the system a basis.
- After changing the TeX source, rebuild and validate the tracked PDF. Commit
  and push the TeX and PDF together unless the user requests otherwise.
