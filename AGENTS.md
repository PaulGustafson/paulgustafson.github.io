# Manuscript style

These rules apply to the manuscript entry point
`Emergent_Mathematics.tex` and its part files
`Emergent_Mathematics_Symmetry.tex`,
`Emergent_Mathematics_Particles.tex`,
`Emergent_Mathematics_Integrable_Probability.tex`,
`Emergent_Mathematics_Integrability.tex`, and
`Emergent_Mathematics_Geometry.tex`.

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

## Application-driven section structure

- Treat each `\section` as a complete mathematical arc rather than as a
  container for prerequisite material.
- Keep section titles short and nonconjunctive. Each title should name one
  principal mathematical subject; do not join subjects or applications with
  "and," commas, ampersands, or multi-clause constructions. Put the detailed
  scope and physical culmination in exercise titles and exercise bodies.
- Give every section exactly four subsections corresponding, in this order,
  to symmetry, decomposition, special functions, and physical predictions.
  Title each subsection by the specific mathematical instance it develops,
  such as `Compact Groups`, `Peter--Weyl Decomposition`, `Wigner Functions`,
  or `Angular Spectroscopy`; do not use the generic component names as
  subsection titles.  Do not add `\subsubsection` or lower-level divisions.
- In the first subsection, specify the group, algebra, group action,
  homogeneous space, or tensor category and what it acts on.  In the second,
  develop the associated spectral, representation-theoretic, transform,
  convolution, or sector decomposition.  In the third, derive the characters,
  matrix coefficients, eigenfunctions, or kernels that make the decomposition
  explicit.  In the fourth, use those functions to calculate quantitative
  observables and state the modeling assumptions.
- Treat the four-subsection structure as a substantive test, not a formatting
  device.  If a section cannot support every stage without unrelated filler,
  refocus it or merge its material into a section that can.
- Every section must culminate in a substantial exercise that derives or uses
  a named special-function family and applies it to a concrete physical
  observable.
- The culminating exercise must extract a quantitative, experimentally
  testable prediction, such as spectral values or spacings, zeros and
  resonance locations, scattering or diffraction intensities, selection
  rules, transition amplitudes, correlation laws, transport coefficients,
  critical exponents, or asymptotic distributions.
- Group characters, spherical functions, orthogonal polynomials,
  hypergeometric functions, transform kernels, and integrable kernels count as
  special functions when their defining identities and analytic role are made
  explicit. Merely mentioning such a function does not satisfy this rule.
- State the mathematical model, normalization conventions, observable, and
  prediction in the exercise. When experimental evidence is cited,
  distinguish the derived prediction, modeling assumptions, measured
  quantity, and limitations of the comparison.
- Foundational material that does not naturally support such a culminating
  exercise must be organized as subsections of the earliest larger section
  that uses it. It should not remain a standalone section.
- Do not append an unrelated special-function example merely to satisfy this
  rule. Merge, rename, reorder, or divide sections so that the culminating
  application follows from the preceding development.
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
