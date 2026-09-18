# Mathematics via Lattice Models: development status

The twelve-part conversion has a buildable exercise draft with the fixed
64-section table of contents in `MANUSCRIPT_CONVENTIONS.md`. The entry point
and PDF retain the filenames `Mathematics_of_Lattice_Models.tex` and
`Mathematics_of_Lattice_Models.pdf`.

| Part | Current development | Final quantitative prediction |
|---|---|---|
| I | Finite Gibbs measures, intrinsic linear algebra, exact chain transfer operator | Brillouin magnetization and chain heat capacity |
| II | Pressure, boundary comparison, DLR states, correlations, Peierls bounds, Lee–Yang, duality | Critical temperature, logarithmic heat capacity, magnetization exponent |
| III | Independent edges, random clusters, planar duality, branching threshold, decay, Loewner scaling | Triangular-site crossing probabilities |
| IV | Ice configurations, spectral parameter, RTT, Yang–Baxter, magnon Bethe equations | Saturation field and one-magnon dispersion |
| V | Hopf action, quantum symmetric powers, Hecke and Temperley–Lieb, intrinsic representation decomposition | Open-chain multiplets and selection rules |
| VI | Theta identities, eight-vertex operator, first fusion relation, RSOS dimensions, dynamical elliptic relation | RSOS strip residual entropy |
| VII | Loop diagrams, fusion paths, Perron–Frobenius, a pointed modular category, braids, bracket invariant | Fibonacci state growth and mutual braiding phase |
| VIII | Pointed fusion categories, intrinsic recoupling, cocycles, finite state sums and gluing | String-net degeneracy and pair-creation gap |
| IX | Finite gauge fields, Wilson loops, flat fields, cocycle action, classifying and cocycle spaces | Wilson area coefficient and higher flux sectors |
| X | Chiral hopping model, winding, bundle classes, ordinary cohomology spectrum | Bulk gap and localized boundary levels |
| XI | One-root rational Bethe state, one-vertex quiver, cotangent projective line, two-chamber stable envelopes | Two-spin exchange splitting |
| XII | Rational Gaudin operators, Bethe states, scalar opers, rank-one dual root data, abelian sphere Hecke eigencondition | Gaudin pair spectroscopy from oper residues |

## Scope for subsequent development

The general subjects have deliberately restricted worked models. Further
development can extend them without changing the table of contents:

- Derive thermodynamic six-vertex spectra beyond the finite magnon sector.
- Extend the verified first fusion relation to a carefully normalized
  higher elliptic fusion hierarchy.
- Develop nonpointed string-net recoupling and state sums beyond the
  group-labelled case.
- Extend the topological-phase treatment beyond chiral one-particle
  Hamiltonians; the current spectrum construction represents ordinary
  cohomology and does not classify general interacting phases.
- Extend stable envelopes beyond the two-fixed-point cotangent projective
  line, and quiver actions beyond the two-site calculation.
- Develop the punctured, nonabelian geometric Langlands correspondence.
  The current Hecke exercise proves the abelian sphere case; the Gaudin
  exercise constructs the rank-one Bethe-to-oper map without asserting a
  general spectral equivalence.

## Validation

Run `bash scripts/build_lattice_manuscript.sh`. It audits the prescribed
headings, exercise-only body, final predictions, bibliography, and placement
of external hypotheses, then runs `pdflatex` three times in a temporary
directory. It replaces the tracked PDF only after checking the generated
TOC, PDF text, unresolved citations, and overfull boxes.

The continuation was also checked against independent finite calculations:
the ordinary and dynamical elliptic Yang–Baxter equations, the first fusion
determinant, Temperley–Lieb relations, RSOS fusion at levels 1–7, a periodic
two-magnon Bethe state, Gaudin commutators and one-root eigenvalues, a
four-plaquette gauge partition function, and hopping-chain boundary
residuals. These are numerical consistency checks, not a complete proof
audit of the manuscript.
