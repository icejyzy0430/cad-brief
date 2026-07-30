# Readiness gates

Read this file immediately before assigning final status. Assign exactly one of
`ready`, `provisional`, or `blocked`.

## Contents

- [Decision order](#decision-order)
- [Ready](#ready)
- [Provisional](#provisional)
- [Blocked](#blocked)
- [Intent-specific minimums](#intent-specific-minimums)
- [Status consistency checks](#status-consistency-checks)

## Decision order

1. Identify the stated intent level.
2. List the controlling requirements for that level.
3. Check their evidence, conflicts, CAD mapping, and validation.
4. Decide whether remaining uncertainty changes topology, fit, manufacture,
   safety, or only delegated/cosmetic choices.
5. Apply the appropriate gate below.

Do not choose status based on the number of dimensions alone. A numeric prompt
can still omit a controlling interface; a visual concept can be useful with few
exact dimensions.

## Ready

Assign `ready` only when all are true:

- target identity and task scope are resolved,
- units and coordinate convention can be declared,
- all critical and required hard constraints have credible sources or exact
  derivations,
- no unresolved conflict controls topology, an interface, or an acceptance
  claim,
- part boundaries and assembly relationships are defined when applicable,
- every controlling interface has geometry, direction, and clearance intent,
- each critical requirement has a CAD mapping,
- each measurable critical requirement has a real TTC validation method,
- visual-only requirements explicitly use snapshot and user review,
- requested deliverables keep STEP primary,
- assumptions affect only delegated, reversible, or non-controlling choices.

`ready` means ready for TTC to model the stated nominal geometry. It does not
mean certified, safe, production-approved, or guaranteed manufacturable.

## Provisional

Assign `provisional` only when all are true:

- a useful concept or parametric approximation can be built honestly,
- the intent permits approximation or the user accepted the downgrade,
- target identity is known or a declared candidate was selected,
- the overall scale is sourced or an explicit nominal design choice,
- every uncertain value, hidden region, and simplified component is identified,
- approximate values can become named, replaceable parameters,
- no missing value is being presented as exact fit, safety, compliance, or
  production evidence,
- the handoff states what future evidence would upgrade the model.

Typical provisional cases:

- a commercial product exterior reconstructed from photos and official overall
  dimensions,
- a concept bracket with delegated cosmetic dimensions,
- a simplified purchased-part envelope,
- hidden surfaces modeled as explicit approximations.

Do not use `provisional` to bypass an unresolved fit-critical interface.

## Blocked

Assign `blocked` when any is true:

- exact fit is requested but a controlling interface is missing or conflicting,
- manufacturing or production use depends on missing material/process geometry,
- safety, load, pressure, medical, or compliance claims lack required engineering
  inputs or external validation,
- product candidates imply materially different geometry and cannot be resolved,
- two hard requirements conflict,
- exact reproduction requires hidden or internal geometry with no evidence,
- a required source file or imported geometry is unavailable,
- the user rejects a provisional downgrade and available evidence cannot support
  the requested accuracy.

For `blocked`:

- preserve all useful confirmed research,
- list blockers and the exact evidence that would clear them,
- include no executable TTC CAD brief,
- include no copy prompt for `$cad`,
- do not continue asking after the two-round limit.

## Intent-specific minimums

### Concept

Require:

- purpose and recognizable topology,
- selected or nominal scale,
- visible identity-critical features,
- explicit freedom and exclusions.

Allow proposed defaults and visual estimates.

### Fit

Additionally require:

- exact mating-object identity or geometry,
- mounting/mating datums and directions,
- controlling dimensions and clearances,
- motion or access envelope when relevant,
- validation targets for every interface.

### Manufacturing-intent

Additionally require geometry-affecting:

- process and material intent,
- wall/stock/sheet thickness,
- relevant tool, nozzle, bend, draft, support, or minimum-feature constraints,
- hole intent such as clearance, tap, press, or locating,
- nominal tolerances only when provided or sourced.

Do not claim process approval.

### Engineering-review

Record:

- load cases and environment,
- applicable standards and factors when supplied,
- required analysis, test, review, and sign-off,
- which items TTC cannot validate.

The nominal CAD handoff may be `ready` only for geometry when engineering claims
are explicitly outside the success criteria. Otherwise return `blocked`.

## Status consistency checks

- `ready` must not contain a critical or required requirement with status
  `unknown` or `conflict`.
- `ready` must not contain a critical hard requirement with status `provisional`.
- `provisional` may contain visual and preferred provisional requirements, but
  not an unresolved critical fit or safety requirement.
- `blocked` must name at least one blocker and must withhold TTC handoff content.
