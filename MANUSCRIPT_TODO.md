# Manuscript Section Audit

For each section, begin from its title alone rather than from the material
currently assigned to it.  Determine the canonical:

1. symmetry;
2. decomposition;
3. special-function family;
4. physical application and quantitative prediction.

Choose the four subsection titles from that canonical arc.  Only afterward
compare the proposed arc with the manuscript, retaining material that belongs,
moving material needed elsewhere, and deleting material that has no natural
place.

## Accepted canonical arcs

- [x] Fourier Analysis

  - **Symmetry:** Locally compact abelian groups acting by translation on
    functions on the group.  The principal examples are
    $\mathbb R^n$, $\mathbb Z^n$, $\mathbb T^n$, $U(1)$, and finite abelian
    groups.  Their irreducible unitary representations are their characters.
  - **Decomposition:** Pontryagin duality and the decomposition of the regular
    representation into characters.  Develop Fourier inversion, Plancherel,
    convolution diagonalization, and Poisson summation for lattices.
  - **Special functions:** The characters $e^{ipx}$, $e^{in\theta}$, and
    $z^n$, together with the Dirichlet kernel, Fejér kernel, sinc function,
    and Gaussian Fourier kernel.  Bessel, Airy, and Pearcey functions require
    additional rotational or singularity structure and are not canonical to
    Fourier analysis itself.
  - **Physical application:** Fraunhofer diffraction.  The aperture amplitude
    is Fourier transformed and the measured intensity is its squared modulus.
    Derive the $\operatorname{sinc}^2$ single-slit envelope, the squared
    Dirichlet kernel for an equally spaced slit array, and reciprocal-lattice
    peaks from Poisson summation, including the predicted minima and peak
    spacings.
  - **Subsection titles:** `Locally Compact Abelian Groups`, `Pontryagin
    Duality`, `Fourier Kernels`, `Fraunhofer Diffraction`.

- [x] Compact Harmonic Analysis

  - **Symmetry:** Compact groups and their finite-dimensional unitary
    representations, with $SU(2)\to SO(3)$ as the principal example.
  - **Decomposition:** The Peter--Weyl theorem, Schur orthogonality, character
    inversion, and the homogeneous-space decomposition of
    $S^2=SO(3)/SO(2)$.
  - **Special functions:** Wigner $D$-functions, including characters,
    spherical harmonics, Legendre polynomials, and Jacobi-polynomial formulas
    for the reduced Wigner functions.
  - **Physical application:** Molecular rotational spectroscopy.  Derive the
    rigid-rotor levels, degeneracies, dipole selection rules, line spacings,
    and Clebsch--Gordan intensity factors.
  - **Subsection titles:** `Compact Groups`, `Peter--Weyl Theorem`, `Wigner
    Functions`, `Rotational Spectroscopy`.

## Proposed canonical arcs

The table of contents uses these proposed subsection titles.  An unchecked
arc has not yet been accepted, and its existing exercises have not yet been
reorganized to match the titles.

- [ ] Coadjoint Orbits

  - **Symmetry:** Hamiltonian Lie-group actions and moment maps.
  - **Decomposition:** Symplectic reduction at coadjoint-orbit values.
  - **Special functions:** Spin coherent states and their reproducing kernels
    on integral $SU(2)$ orbits.
  - **Physical application:** Spin precession, including the Larmor frequency
    and coherent-state transition probabilities.
  - **Subsection titles:** `Hamiltonian Group Actions`, `Symplectic Reduction`,
    `Spin Coherent States`, `Spin Precession`.

- [ ] Heisenberg Group

  - **Symmetry:** Central extensions of phase-space translations and the Weyl
    commutation relations.
  - **Decomposition:** The Stone--von Neumann theorem and the fixed-central-
    character representation.
  - **Special functions:** Hermite functions as oscillator matrix
    coefficients and eigenfunctions.
  - **Physical application:** Harmonic-oscillator spectroscopy, including
    equally spaced levels and ladder-operator transition strengths.
  - **Subsection titles:** `Central Extensions`, `Stone--von Neumann Theorem`,
    `Hermite Functions`, `Oscillator Spectroscopy`.

- [ ] Poincaré Group

  - **Symmetry:** The isometry group of Minkowski spacetime and its spin cover.
  - **Decomposition:** Wigner's classification by mass and little-group
    representation.
  - **Special functions:** Lorentz-invariant Bessel kernels obtained from
    mass-shell Fourier transforms.
  - **Physical application:** Relativistic propagation, including dispersion,
    causal support, and mass-dependent arrival-time predictions.
  - **Subsection titles:** `Minkowski Isometries`, `Wigner Classification`,
    `Bessel Functions`, `Relativistic Propagation`.

- [ ] Potential Scattering

  - **Symmetry:** The $SO(3)$ action preserved by a central potential.
  - **Decomposition:** Partial-wave decomposition into angular-momentum
    channels and phase shifts.
  - **Special functions:** Regular and irregular Coulomb wave functions and
    their Legendre partial-wave expansion.
  - **Physical application:** Rutherford scattering, including the angular
    cross section and detector-count prediction.
  - **Subsection titles:** `$SO(3)$`, `Partial-Wave Decomposition`, `Coulomb
    Functions`, `Rutherford Scattering`.

- [ ] Schwarzschild Spacetime

  - **Symmetry:** Time translations and rotations of Schwarzschild spacetime.
  - **Decomposition:** Regge--Wheeler separation into frequency,
    angular-momentum, and parity sectors.
  - **Special functions:** Confluent Heun functions for the separated radial
    equations.
  - **Physical application:** Black-hole ringdown through quasinormal-mode
    frequencies and damping times.
  - **Subsection titles:** `Schwarzschild Isometries`, `Regge--Wheeler
    Decomposition`, `Confluent Heun Functions`, `Black-Hole Ringdown`.

- [ ] Determinantal Kernels

  - **Symmetry:** Unitary conjugation of Hermitian operators.
  - **Decomposition:** The Weyl integration formula separating unitary orbits
    from eigenvalues and producing the Vandermonde density.
  - **Special functions:** Hermite Christoffel--Darboux kernels and their sine
    and Airy scaling limits.
  - **Physical application:** Quantum-chaotic spectra in the unitary symmetry
    class, including level repulsion and local correlation laws.
  - **Subsection titles:** `Unitary Groups`, `Weyl Integration Formula`,
    `Hermite Kernels`, `Quantum-Chaotic Spectra`.

- [ ] Transfer Matrices

  - **Symmetry:** Global $\mathbb Z_2$ spin-flip symmetry of the Ising model.
  - **Decomposition:** Transfer-matrix spectral sectors and correlation
    lengths.
  - **Special functions:** Theta functions encoding finite-size Ising
    partition functions and scaling characters.
  - **Physical application:** Ising criticality, including the critical
    temperature, correlation length, and finite-size spectrum.
  - **Subsection titles:** `$\mathbb Z_2$ Spin Symmetry`, `Transfer-Matrix
    Spectrum`, `Theta Functions`, `Ising Criticality`.

- [ ] $SL_2(\mathbb R)$

  - **Symmetry:** The transitive $SL_2(\mathbb R)$ action on the hyperbolic
    plane with stabilizer $SO(2)$.
  - **Decomposition:** The unitary dual and Plancherel decomposition into
    principal, complementary, and discrete series.
  - **Special functions:** Legendre and Mehler--Fock spherical functions.
  - **Physical application:** Hyperbolic-drum spectra and resonance phase
    fronts determined by Legendre-function boundary conditions.
  - **Subsection titles:** `Hyperbolic Isometries`, `Unitary Dual`, `Legendre
    Functions`, `Hyperbolic-Drum Spectra`.

- [ ] $SL_2(\mathbb Z)$

  - **Symmetry:** The modular group acting on the upper half-plane.
  - **Decomposition:** The automorphic spectrum into cuspidal, residual, and
    Eisenstein contributions.
  - **Special functions:** Modular forms, including Eisenstein series, theta
    functions, eta functions, and modular characters.
  - **Physical application:** Two-dimensional conformal spectra constrained
    by modular invariance and finite-size partition functions.
  - **Subsection titles:** `Modular Group`, `Automorphic Spectrum`, `Modular
    Forms`, `Conformal Spectra`.

- [ ] Quantum Groups

  - **Symmetry:** The quasitriangular Hopf algebra
    $U_q(\mathfrak{sl}_2)$ and its compact dual $SU_q(2)$.
  - **Decomposition:** Quantum Peter--Weyl theory, tensor-product
    decomposition, and the universal $R$-matrix.
  - **Special functions:** Basic hypergeometric functions and the
    $q$-orthogonal polynomials appearing as quantum coupling coefficients.
  - **Physical application:** The XXZ spin-chain spectrum, Bethe equations,
    and transition strengths.
  - **Subsection titles:** `$U_q(\mathfrak{sl}_2)$`, `Quantum Peter--Weyl
    Theorem`, `Basic Hypergeometric Functions`, `XXZ Spectroscopy`.

- [ ] Double Affine Hecke Algebras

  - **Symmetry:** Double-affine braid groups and their Hecke quotients.
  - **Decomposition:** Cherednik's polynomial representation and commuting
    difference operators.
  - **Special functions:** Macdonald polynomials, including the rank-one
    Askey--Wilson family and standard degenerations.
  - **Physical application:** The Ruijsenaars--Schneider spectrum and its
    Calogero--Sutherland limit.
  - **Subsection titles:** `Double-Affine Braid Groups`, `Polynomial
    Representation`, `Macdonald Polynomials`, `Ruijsenaars--Schneider
    Spectrum`.

- [ ] Algebraic Curves

  - **Symmetry:** Translation by the algebraic group law on an elliptic curve.
  - **Decomposition:** The realization of genus-one curves as branched double
    covers of the projective line.
  - **Special functions:** Complete elliptic integrals and their period
    relations.
  - **Physical application:** The amplitude-dependent period of the nonlinear
    pendulum.
  - **Subsection titles:** `Elliptic-Curve Translations`, `Branched Covers`,
    `Elliptic Integrals`, `Pendulum Periods`.

- [ ] Riemann--Roch

  - **Symmetry:** The Picard group acting on line bundles by tensor product.
  - **Decomposition:** Sheaf cohomology and the Riemann--Roch index
    $h^0-h^1$.
  - **Special functions:** Theta functions as explicit sections of positive
    line bundles on complex tori.
  - **Physical application:** Landau levels on a torus, including flux
    degeneracy and magnetic-translation constraints.
  - **Subsection titles:** `Picard Group`, `Sheaf Cohomology`, `Theta
    Functions`, `Landau Levels`.

- [ ] Affine Grassmannian

  - **Symmetry:** Loop groups acting on the affine Grassmannian.
  - **Decomposition:** The geometric Satake equivalence built from Schubert
    strata and perverse-sheaf convolution.
  - **Special functions:** Weyl characters obtained as the categorical
    spherical functions of Satake convolution.
  - **Physical application:** Fusion and magnetic-charge selection rules for
    't Hooft line operators.
  - **Subsection titles:** `Loop Groups`, `Geometric Satake Equivalence`, `Weyl
    Characters`, `'t Hooft-Line Fusion`.

- [ ] Finite-Gap Spectral Curves

  - **Symmetry:** Commuting KdV flows preserving the spectral curve.
  - **Decomposition:** Bloch--Floquet decomposition and linearization of the
    flows on the spectral Jacobian.
  - **Special functions:** Baker--Akhiezer functions and their theta-function
    formulas.
  - **Physical application:** Band-gap spectroscopy, including band edges,
    attenuation exponents, and cnoidal-wave transport.
  - **Subsection titles:** `KdV Flows`, `Bloch--Floquet Decomposition`,
    `Baker--Akhiezer Functions`, `Band-Gap Spectroscopy`.

- [ ] Index Theory

  - **Symmetry:** $U(1)$ gauge transformations of coupled Dirac operators.
  - **Decomposition:** The Atiyah--Singer theorem relating analytic zero-mode
    sectors to the topological symbol class.
  - **Special functions:** Monopole harmonics for the coupled spherical Dirac
    and Landau operators.
  - **Physical application:** Quantized Hall conductance and flux-controlled
    Landau-level degeneracy.
  - **Subsection titles:** `$U(1)$ Gauge Symmetry`, `Atiyah--Singer Theorem`,
    `Monopole Harmonics`, `Quantum Hall Conductance`.

- [ ] Cobordism

  - **Symmetry:** Oriented, spin, and complex tangential structures associated
    with $SO$, $\operatorname{Spin}$, and $U$.
  - **Decomposition:** The Pontryagin--Thom theorem identifying bordism groups
    with stable homotopy groups of Thom spectra.
  - **Special functions:** Spectral eta functions and eta invariants defining
    bordism-sensitive phases.
  - **Physical application:** SPT phases, including bulk partition phases and
    boundary spectral asymmetry.
  - **Subsection titles:** `$SO$, $\operatorname{Spin}$, and $U$ Structures`,
    `Pontryagin--Thom Theorem`, `Eta Functions`, `SPT Phases`.

- [ ] Fusion Categories

  - **Symmetry:** Temperley--Lieb categories as concrete noninvertible
    symmetries.
  - **Decomposition:** Root-of-unity semisimplification into finitely many
    simple fusion sectors.
  - **Special functions:** The modular $S$-matrix as a categorical Fourier
    kernel diagonalizing the fusion rules.
  - **Physical application:** Anyon interferometry, including fusion-channel
    probabilities and interference amplitudes.
  - **Subsection titles:** `Temperley--Lieb Categories`, `Fusion
    Semisimplification`, `Modular $S$-Matrix`, `Anyon Interferometry`.
