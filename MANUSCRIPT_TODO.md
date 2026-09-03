# Manuscript section audit

The manuscript is ordered by special-function families.  Within every
section the exercises develop the geometric symmetry that produces the
family, its decomposition theorem, and a quantitative physical observable.
The twenty-four sections are grouped into seven parts; subsection and
lower-level headings are deliberately omitted.

| Part | Sections |
|---|---|
| Harmonic Analysis | Fourier Kernels through Bessel Functions |
| Hypergeometric Functions | Gauss Hypergeometric Functions through Heun Functions |
| Character Theory | Weyl Characters through Affine Characters |
| $q$-Series | Basic Hypergeometric Functions through Macdonald Polynomials |
| Algebraic Geometry | Elliptic Functions through Baker--Akhiezer Functions |
| Algebraic Topology | Monopole Harmonics and Eta Functions |
| Tensor Categories | Hall--Littlewood Polynomials and Modular $S$-Matrices |

| Section | Geometric symmetry | Special-function decomposition | Physical observable |
|---|---|---|---|
| Fourier Kernels | LCA translations on $G$ | Pontryagin decomposition with Gaussian, Dirichlet, and sinc kernels | Rectangular diffraction |
| Wigner Functions | Compact-group and $SU(2)$ orbit symmetry | Peter--Weyl, Wigner, and Krawtchouk decompositions | Rotational and spin spectroscopy |
| Jacobi Functions | $O(d+1)$ acting on $S^d$ | Jacobi--Gegenbauer spherical decomposition | Spherical-resonator spectra |
| Hermite Functions | Central phase-space translations | Stone--von Neumann decomposition and the Mehler kernel | Oscillator spectroscopy |
| Determinantal Kernels | $U(W)$ acting on Hermitian endomorphisms | Orthogonal-polynomial, sine, and Airy kernels | Quantum-chaotic spectra |
| Bessel Functions | Euclidean, Poincaré, and radial rotation symmetry | Hankel, mass-shell, and partial-wave decompositions | Diffraction, correlations, and hard-sphere scattering |
| Gauss Hypergeometric Functions | Asymptotic translations of the line | Jost decomposition and Gauss connection formulas | Reflectionless transmission |
| Legendre Functions | $SL_2(\mathbb R)$ acting on $\mathbb H$ | Unitary dual and Mehler--Fock decomposition | Hyperbolic-drum spectra |
| Kummer Functions | $SO(4)$ dynamical symmetry | Kummer, Laguerre, and Coulomb spectral functions | Hydrogen and Rutherford observables |
| Heun Functions | $\mathbb R\times SO(3)$ acting on Schwarzschild spacetime | Regge--Wheeler, Heun, and parabolic-cylinder modes | Scalar ringdown |
| Weyl Characters | Weyl symmetry of reductive weight spaces | Highest weights, Weyl characters, and Schur functions | Flavor multiplets |
| Automorphic Forms | $SL_2(\mathbb Z)$ acting on $\mathbb H$ | Eisenstein, theta, eta, and automorphic spectral decomposition | Cusp scattering |
| Virasoro Characters | $\operatorname{Diff}^+(S^1)$ and Ising spin reversal | Virasoro, Toeplitz, and Ising character decompositions | Critical and finite-size spectra |
| Affine Characters | $LK_c\rtimes S^1$ acting on loop fields | Weyl--Kac characters and KZ conformal blocks | WZW finite-size spectra |
| Basic Hypergeometric Functions | $U_v(\mathfrak{sl}_2)$ acting on tensor products | Quantum Peter--Weyl, $q$-Hahn, and $q$-Racah functions | XXZ spectroscopy |
| Jack Polynomials | Reflection groups acting on Euclidean space | Dunkl, generalized-Bessel, and Jack decomposition | Calogero--Sutherland spectroscopy |
| Macdonald Polynomials | DAHA acting on an algebraic torus | Cherednik, Macdonald, and Askey--Wilson decomposition | Ruijsenaars spectrum |
| Elliptic Functions | Elliptic translations on complex tori | Abel--Jacobi inversion and elliptic functions | Nonlinear-pendulum periods |
| Bergman Kernels | $\operatorname{Aut}(X,L)$ acting on sections | Riemann--Roch, localization, and Bergman projection | Landau-level density |
| Baker--Akhiezer Functions | Translations and KdV flows on periodic potentials | Theta, Baker--Akhiezer, and Bloch--Floquet decomposition | Band-gap spectroscopy |
| Monopole Harmonics | Gauge symmetry of connections and coupled operators | Index decomposition and monopole harmonics | Integer Hall conductance |
| Eta Functions | Frame symmetry and tangential structures | Pontryagin--Thom and eta-spectral decomposition | Invertible-phase response |
| Hall--Littlewood Polynomials | $G[[z]]$ acting on affine-Grassmannian modifications | Satake convolution and Hall--Littlewood decomposition | 't Hooft fusion |
| Modular $S$-Matrices | Fusion categories acting on fusion state spaces | Modular sine transform and Verlinde decomposition | Anyon interferometry |

## Validation checklist

- [x] The section order follows special-function families rather than a list
      of high-level structures.
- [x] Every definition occurs at first use inside an exercise.
- [x] No standalone motivational or transitional prose appears in the body.
- [x] No theorem is designated as supplied or assumed input.
- [x] Every section specifies an acting symmetry and the space on which it acts.
- [x] Every named special-function system occurs with an orthogonality,
      completeness, inversion, kernel, or spectral-resolution identity.
- [x] Every final exercise uses the section's special-function decomposition
      to calculate a stated physical observable.
- [x] Fourier, metric-signature, Laplacian, modular-nome, quantum, elliptic,
      and Clifford conventions are explicit and nonconflicting.
- [x] Rebuild the PDF and repeat the structural audit after every source change.
