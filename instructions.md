# Exercise-First Authoring Conventions

## Governing principle

Definitions establish the language; exercises carry the mathematics and
physics.

The exposition should be a concise sequence of indispensable definitions,
notation, conventions, and hypotheses. Every theorem, substantive
consequence, physical derivation, and major application belongs in an
exercise.

## What belongs in the exposition

Prose outside exercises may contain only:

- definitions of objects, maps, equivalences, and constructions;
- notation and standing conventions;
- hypotheses shared by several exercises;
- formulas that are part of a definition or physical setup;
- minimal connective sentences needed to introduce the next definition.

Definitions may include axioms and immediate definitional equalities. They
should not contain embedded proofs or consequences that require proof.

Historical or experimental context should normally be incorporated into an
exercise title or task. A rare one-sentence note is acceptable only when it
cannot reasonably be made into a mathematical task and is essential for
orientation.

## What must be an exercise

Move a statement into an exercise whenever it asserts any of the following:

- existence, uniqueness, or classification;
- an identity, inequality, equivalence, or invariance property;
- functoriality or independence from a choice;
- a decomposition, reconstruction, or comparison theorem;
- a conservation law or equation derived from an action or symmetry;
- a physical prediction, selection rule, observable phase, or experimental
  consequence;
- an application of the definitions to a significant example.

In particular, statements naturally beginning with *prove*, *show*,
*deduce*, *verify*, *classify*, or *interpret* belong in exercises.

Do not use theorem, proposition, lemma, corollary, proof, solution, or hint
environments. Difficulty is not a reason to state a result in the prose.

## Exercise titles

Use short, informative titles that name the result or physical conclusion.
Prefer declarative titles when they can carry motivation that would otherwise
require an expository sentence.

Good examples include:

- `The top exterior power is one-dimensional`
- `Averaging produces invariant projections and inner products`
- `Water has three symmetry-classified vibrations`
- `Nontrivial cohomology produces the Aharonov--Bohm phase`
- `Gauge invariance forces charge conservation`
- `K-theory classifies class A band insulators`
- `Every entangled pure two-qubit state violates CHSH`
- `Subfactor indices below four are quantized`

Avoid vague titles such as `Properties`, `Calculation`, or `Application`.
Put precise hypotheses and the full mathematical statement in the exercise
body rather than overloading the title.

## Deep results

Use one of these formats for results whose full proof requires substantial
machinery:

1. State the complete theorem as an exercise when it is central and
   intelligible from the preceding definitions.
2. Put an explicitly assumed theorem inside an exercise and ask for the
   consequences needed by the document.
3. Use a finite-dimensional, compact, bounded, or otherwise accessible
   special case that preserves the conceptual point.

Never move a deep result into exposition merely because the exercise is
difficult.

## Exercise quality and organization

Exercises should be theorem-sized. Prefer exercises that establish a central
result, connect several definitions, derive a physical consequence, or bridge
to the next subsection. Break long results into meaningful intermediate
prompts, but do not create exercises that only repeat a definition or perform
routine substitution.

Within a subsection, collect the elementary theory before its principal
application. A physical symmetry group should arise from a stated symmetry of
a system; if a model instead takes the group from experiment, identify it
explicitly as empirical input rather than presenting it as a consequence of
the preceding mathematics.

The document's main progression is:

1. **Algebra:** coordinate-free linear algebra, representation theory, Lie
   theory, and braided tensor categories.
2. **Geometry:** forms and cohomology, bundles and K-theory, symplectic
   geometry, connections and curvature, gauge theory, Chern--Simons theory,
   and TQFT.
3. **Analysis:** Hilbert-space operator theory, quantum information and Bell
   inequalities, von Neumann algebras, subfactors, and Jones theory.

The prose should define the structures supporting this progression; the
exercises should establish all links between them.

## Physics and experimental claims

The exposition may define a state, observable, transition amplitude, field,
action, symmetry group, connection, Hamiltonian, or physical model. Exercises
must derive the resulting:

- equations of motion and conservation laws;
- allowed and forbidden transitions;
- vibrational modes and spectroscopic activity;
- Berry and Aharonov--Bohm phases;
- topological classifications and invariants;
- symmetry breaking and particle charges or masses;
- entanglement tests and Bell violations;
- braid statistics, skein relations, and knot invariants.

When an experiment motivates a construction, name the observable conclusion
in the exercise title and place any comparison with cited data inside the
exercise.

## Citation policy

Inline citations are exceptional. Use them only for:

- primary sources reporting experiments or observations discussed by an
  exercise;
- original or authoritative sources for major theorems, classifications, or
  constructions that form a destination of an exercise;
- a specialized formula or data set whose provenance a reader could not
  reasonably infer.

Place a theorem citation in the exercise that states the result, and place an
experimental citation in the task that compares the mathematical prediction
with the observation. Do not attach citations to routine definitions,
standard notation, elementary constructions, or textbook-level background
such as vector spaces, tensor and exterior algebras, manifolds, differential
forms, representations, or Hilbert spaces.

Prefer one primary source to a cluster of general references. Remove
bibliography entries that are no longer cited unless the document explicitly
labels them as further reading.

## Cross-references

Definitions may refer forward to exercises, and exercises may invoke earlier
definitions. A forward reference may preview a later application, but it must
not supply a definition, hypothesis, or result needed to solve the current
exercise. State any such prerequisite locally inside the exercise. When a
later section develops the full application, make it refer backward to the
earlier exercise.

Use concise references such as `By Exercise~\ref{...}` or
`Apply Exercise~\ref{...}`. Do not restate an exercise's conclusion afterward
unless it is required to define the next object.

## Editorial audit

For every declarative sentence outside an exercise, ask:

1. Is it a necessary definition, convention, hypothesis, or transition?
2. Does it assert something that a reader could reasonably be asked to prove,
   derive, verify, classify, or interpret?

If the answer to the second question is yes, move it into an exercise. If the
answer to both questions is no, delete it.

Before finalizing a subsection, verify that:

- every object is defined before use;
- no exercise depends on definitions or hypotheses introduced only in a later
  section;
- every substantive mathematical or physical claim occurs in an exercise;
- every exercise has an informative title;
- no theorem or proof environments remain;
- no solutions or hints are included;
- coordinate calculations appear only when they reveal an invariant or an
  important physical consequence;
- the subsection ends with an exercise that advances the document's main
  conceptual arc.
