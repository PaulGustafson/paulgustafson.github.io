# Manuscript section audit

Every section is organized internally as geometric symmetry, special-function
decomposition, and physical predictions. The sections are grouped into eight
parts; subsection and lower-level headings are deliberately omitted.

| Part | Sections |
|---|---|
| Harmonic Analysis | Hilbert Space through Poincaré Group |
| Scattering Theory | One-Dimensional Scattering through Schwarzschild Spacetime |
| Hyperbolic Geometry | $SL_2(\mathbb R)$ and $SL_2(\mathbb Z)$ |
| Conformal Field Theory | Virasoro Algebra and Ising Model |
| Quantum Algebra | Affine Kac--Moody Algebras through Double Affine Hecke Algebras |
| Algebraic Geometry | Algebraic Curves through Finite-Gap Spectral Curves |
| Algebraic Topology | Index Theory and Cobordism |
| Tensor Categories | Geometric Satake and Fusion Categories |

| Section | Geometric symmetry | Special-function decomposition | Physical prediction |
|---|---|---|---|
| Hilbert Space | $U(A)_h$ acting on projective state space | Spectral theorem and Green functions | Resonance spectroscopy |
| Fourier Analysis | LCA translations on $G$ | Pontryagin duality and Fourier kernels | Fraunhofer diffraction |
| Peter--Weyl Theory | $K\times K$ acting on $K$ | Peter--Weyl decomposition and Wigner functions | Rotational spectroscopy |
| Reductive Groups | Weyl group acting on weight space | Highest weights and Weyl characters | Flavor multiplets |
| Coadjoint Orbits | $G$ acting on symplectic manifolds and orbits | Symplectic reduction and coherent-state kernels | Spin precession |
| Heisenberg Group | Central extension acting on symplectic phase space | Stone--von Neumann decomposition and Hermite functions | Oscillator spectroscopy |
| Unitary Ensembles | $U(W)$ acting on Hermitian endomorphisms | Weyl integration and Hermite/sine/Airy kernels | Quantum-chaotic spectra |
| Poincaré Group | Poincaré group acting on Minkowski spacetime | Wigner classification and Bessel functions | Correlation length |
| One-Dimensional Scattering | Translations acting on the configuration line | Jost decomposition and Pöschl--Teller hypergeometric functions | Transmission and bound-state spectra |
| Potential Scattering | $SO(3)$ acting on $\mathbb R^3$ | Partial waves and Coulomb functions | Rutherford scattering |
| Schwarzschild Spacetime | $\mathbb R\times SO(3)$ acting on the exterior | Regge--Wheeler modes, Heun functions, and parabolic-cylinder functions | Scalar ringdown frequencies and damping times |
| $SL_2(\mathbb R)$ | $SL_2(\mathbb R)$ acting on $\mathbb H$ | Unitary dual, Legendre functions, and the Mehler--Fock transform | Hyperbolic-drum spectra |
| $SL_2(\mathbb Z)$ | $SL_2(\mathbb Z)$ acting on $\mathbb H$ | Automorphic spectrum, Eisenstein series, and modular forms | Cusp-scattering resonances |
| Virasoro Algebra | $\operatorname{Diff}^+(S^1)$ acting on circle fields | Positive-energy modules and Virasoro characters | Conformal finite-size spectra |
| Ising Model | $\mathbb Z_2$ acting on spin configurations | Transfer spectrum, Toeplitz determinants, and Ising characters | Criticality |
| Affine Kac--Moody Algebras | $LK_c\rtimes S^1$ acting on loop fields | Integrable modules, Weyl--Kac characters, and KZ blocks | WZW finite-size spectra |
| Quantum Groups | $U_v(\mathfrak{sl}_2)$ acting on tensor-product state spaces | Quantum Peter--Weyl decomposition and basic hypergeometric functions | XXZ spectroscopy |
| Double Affine Hecke Algebras | DAHA difference-reflection symmetry on an algebraic torus | Cherednik operators and Macdonald polynomials | Ruijsenaars spectrum |
| Algebraic Curves | Elliptic curve acting on itself by translations | Abel--Jacobi decomposition and elliptic functions | Pendulum periods |
| Riemann--Roch | $\operatorname{Aut}(X,L)$ acting on sections | Sheaf cohomology, localization, and Bergman kernels | Landau-level degeneracy and density |
| Finite-Gap Spectral Curves | Translations and KdV flows acting on periodic potentials | Spectral curves, Baker--Akhiezer functions, and Bloch--Floquet theory | Band gaps |
| Index Theory | Gauge group acting on connections and coupled operators | Analytic/topological index and monopole harmonics | Hall conductance |
| Cobordism | Frame-group symmetry and tangential structures | Pontryagin--Thom theory and eta functions | Invertible-phase response |
| Geometric Satake | $G[[z]]$ acting on affine-Grassmannian modifications of 't Hooft defects | Schubert convolution, the Satake equivalence, and Hall--Littlewood polynomials | 't Hooft fusion channels and junction multiplicities |
| Fusion Categories | Fusion category acting on fusion state spaces | Semisimplification, modular $S$-matrix, and Verlinde decomposition | Anyon interferometry |

## Validation checklist

- [x] Every definition occurs at first use inside an exercise.
- [x] No standalone motivational or transitional prose appears in the body.
- [x] No theorem is designated as supplied or assumed input.
- [x] Every section specifies an acting symmetry, its geometric or state
      space, and the invariant structure or operator used in the decomposition.
- [x] Every named special-function system occurs with an orthogonality,
      completeness, inversion, kernel, or spectral-resolution identity.
- [x] Every final exercise uses the section's special-function decomposition
      to calculate a stated physical prediction.
- [x] Hermite, determinant, Fredholm, and representation-theoretic
      prerequisites have a single owner; one-variable, Jacobi, and
      higher-genus theta functions occur as explicit successive extensions.
- [x] Fourier, metric-signature, Laplacian, modular-nome, quantum, elliptic,
      and Clifford conventions are explicit and nonconflicting.
- [x] Full LaTeX build and PDF structural audit.
