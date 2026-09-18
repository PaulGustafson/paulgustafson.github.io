# Manuscript conventions

These rules govern `Mathematics_of_Lattice_Models.tex` and its part files
`Lattice_Models_P01.tex` through `Lattice_Models_P12.tex`.

1. Apart from front matter, sectioning commands, and the bibliography, every
   manuscript passage belongs to an `exercise` environment.
2. Definitions, hypotheses, notation, and normalization conventions occur at
   the beginning of the first exercise that uses them. There are no standalone
   definition environments.
3. Exercises contain the mathematical and physical development. Physical
   motivation must take the form of a concrete calculation, construction,
   comparison, or inference from specified data.
4. Transitions are made by exercise sequence: an exercise at a boundary must
   expose the question, obstruction, or construction used in the next
   section. Free-standing transitional prose is not used.
5. The manuscript has no theorem, observation, remark, example, or proof
   environments. Experimental facts may occur as data in an exercise, but not
   as a separate observations list.
6. No result is declared "supplied," "used without proof," or a theorem to be
   assumed, except that the final prediction exercise of a part may adopt a
   cited theorem as an explicit hypothesis ("assume, as proved by ..."). An
   exercise must otherwise be solvable from earlier material and hypotheses
   stated as mathematical data. Material that requires an undeveloped deep
   theorem is restricted or omitted rather than presented as a citation
   disguised as an exercise.
7. Citations may identify data or invite comparison with a source inside an
   exercise; they may not substitute for an argument required by the exercise.
8. The manuscript and table of contents use part and section headings only;
   there are no subsection or lower-level headings.
9. Part titles name lattice models; section titles name the mathematical
   subjects those models force. Both are the fixed table of contents below.
10. Every part realizes, through its exercise sequence and without printing
    generic stage headings, the progression model, mathematical structure,
    physical prediction, and ends with a quantitative experimentally testable
    prediction.
11. Each notion is defined once, in its owner section, and is used by later
    sections by naming that section. No `\label`/`\ref`.
12. Notation is fixed across parts: inverse temperature $\beta$, coupling
    $J$, $K=\beta J$, field $h$; magnetization exponent $\beta_{\mathrm{mag}}$;
    cluster weight $Q$ and bond density $p$ (Part III); quantum parameter $q$,
    anisotropy $\Delta=\cosh\eta$, loop value $d=q+q^{-1}$; elliptic nome
    $p=e^{\mathrm{i}\pi\tau}$ (Part VI only); gauge coupling $\beta_g$.

## Table of contents (fixed)

| Part | Sections |
|---|---|
| I. Independent Spins / Ising Chain | Microstates, Hamiltonians, partition functions; Gibbs measures; $\log Z$, cumulants, entropy, free energy; Transfer matrices |
| II. 2D Ising Model | Thermodynamic limit; Boundary conditions; Gibbs states; Correlation functions; Phase transitions; Lee--Yang zeros; High/low-temperature expansions |
| III. Percolation / Random-Cluster Model | Probability on lattices; Connectivity; Critical phenomena; Correlation length; Scaling and universality; SLE / conformal invariance |
| IV. Six-Vertex Model | Row-to-row transfer matrices; Spectral parameter; Commuting families; Yang--Baxter equation; Bethe ansatz |
| V. XXZ / Vertex Models | Quantum groups; $U_q(\mathfrak{sl}_2)$; Hecke / Temperley--Lieb algebras; Representation theory; Rational/trigonometric hierarchy |
| VI. Eight-Vertex / RSOS Models | Theta and elliptic functions; Elliptic $R$-matrices; Fusion; Quantum dimensions; Elliptic quantum groups |
| VII. Loop Models / Anyonic Chains | Temperley--Lieb; Fusion graphs; Perron--Frobenius; Modular tensor categories; Braid group representations; Knot invariants |
| VIII. String-Net / State-Sum Models | Fusion categories; $6j$-symbols; Pentagon identities; Turaev--Viro; TQFT |
| IX. Lattice Gauge Theory | Gauge fields on edges; Wilson loops; Flat connections; Dijkgraaf--Witten; Classifying spaces; Higher gauge theory; Homotopy types |
| X. Topological Lattice Phases | Gapped Hamiltonians; Deformation classes of phases; Generalized cohomology; Stable homotopy theory |
| XI. Quiver / Spin-Chain Models | Bethe ansatz; Quiver varieties; Cohomology and $K$-theory; Stable envelopes; Geometric representation theory |
| XII. Gaudin Model | Commuting Hamiltonians; Bethe equations; Opers; Langlands duality; Geometric Langlands |

Structural audits and a successful LaTeX build are required before changes to
the manuscript are committed. Build with `pdflatex` run three times on
`Mathematics_of_Lattice_Models.tex`. The reproducible command
`bash scripts/build_lattice_manuscript.sh` performs the source audit,
three passes, and PDF checks before updating the tracked PDF.
