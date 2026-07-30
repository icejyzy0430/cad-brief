# Requirements contract

Read this file before writing every final requirements package. Use the exact
headings and metadata keys so the bundled validator can check the handoff.

## Contents

- [File name and location](#file-name-and-location)
- [Fixed metadata](#fixed-metadata)
- [Required sections](#required-sections)
- [Sources table](#sources-table)
- [Research and derivation notes](#research-and-derivation-notes)
- [Overall geometry and coordinates](#overall-geometry-and-coordinates)
- [Parameters table](#parameters-table)
- [Parts and components](#parts-and-components)
- [Requirements table](#requirements-table)
- [Interfaces and positioning](#interfaces-and-positioning)
- [Manufacturing intent](#manufacturing-intent)
- [Recommended attachments](#recommended-attachments)
- [Assumptions and delegated choices](#assumptions-and-delegated-choices)
- [Conflicts and blocking unknowns](#conflicts-and-blocking-unknowns)
- [Limitations](#limitations)
- [Completion check](#completion-check)

## File name and location

Write the package in the user's current workspace as:

```text
<suggested-basename>.cad-requirements.md
```

Use a lowercase filesystem-safe basename containing only letters, digits,
hyphens, and underscores. Do not write output into the installed skill folder.

## Fixed metadata

Start with:

```markdown
# CAD Requirements Contract

- Contract version: 1
- Status: ready | provisional | blocked
- Intent level: concept | fit | manufacturing-intent | engineering-review
- Suggested basename: <safe basename>
- Target: <object and exact model/variant when known>
- Task type: new part | assembly | modification
- Primary output: STEP
- Secondary outputs: <none or requested STL/3MF/GLB>
- Question rounds used: 0 | 1 | 2
- Research performed: yes | not-applicable | unavailable
```

Keep the contract version and enum values in English. Write descriptive content
in the user's language.

Use `Research performed: not-applicable` only when the user's supplied
specification is self-contained and no public fact affects it. Use `unavailable`
when research was needed but the host could not perform it; this normally lowers
readiness.

## Required sections

Every package includes these sections in this order:

```text
## Purpose and scope
## Sources
## Research and derivation notes
## Overall geometry and coordinates
## Parameters
## Parts and components
## Requirements
## Interfaces and positioning
## Manufacturing intent
## Recommended attachments
## Assumptions and delegated choices
## Conflicts and blocking unknowns
## Limitations
```

For `ready` and `provisional`, append:

```text
## TTC CAD brief
## Copy prompt for TTC
```

For `blocked`, append this instead:

```text
## TTC handoff withheld
```

Do not include an executable CAD brief or `$cad` prompt in a blocked package.

## Sources table

Use this exact header:

```markdown
| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User request | user | purpose and target | Confirmed in current task |
```

Create a source row for the user request and every attachment or external source
that supports a fact. Use direct URLs or portable attachment filenames. State
model, revision, measurement boundary, and access date when relevant.

## Research and derivation notes

Summarize only research that changes requirements or readiness. For derivations,
show the cited inputs, relation, units, result, and appropriate rounding.

List rejected product candidates when their distinction is material. Do not
expose private chain-of-thought.

## Overall geometry and coordinates

Declare:

- units,
- origin or functional datum,
- base plane and up axis,
- expected envelope and what it includes,
- symmetry or primary axes,
- selected configuration or pose.

If these are downstream design choices, label them as proposed defaults.

## Parameters table

Use:

```markdown
| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
```

Prefer names that can become readable Python parameters. Separate input
parameters from exact derived values. Every provisional dimension should be easy
to replace later.

## Parts and components

Describe part boundaries before features. Use:

```markdown
| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
```

Mark separately manufactured, purchased, or movable parts as separate bodies or
assembly occurrences. Use `Not applicable: single monolithic part` when this
section has no table rows.

## Requirements table

Use this exact header:

```markdown
| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Allowed values:

- Type: `hard`, `functional`, `visual`, `negative`, `manufacturing`
- Priority: `critical`, `required`, `preferred`
- Evidence state: `user-confirmed`, `official-source`,
  `dimensioned-source`, `exactly-derived`, `calibrated-image`,
  `visual-estimate`, `proposed-default`, `unknown`, `conflict`
- Status: `confirmed`, `derived`, `provisional`, `unknown`, `conflict`

Use comma-separated `SRC-###` identifiers in Source. Every referenced source must
exist in the Sources table.

Keep each row evidence-homogeneous. If one feature contains both a confirmed
dimension and an assumed implementation convention, create separate requirement
or parameter rows with their own evidence states. Do not label the combined
statement `user-confirmed`.

CAD mapping examples:

- `named parameter: plate_width`
- `subtractive feature: mounting_holes`
- `named datum: base_mount_plane`
- `assembly occurrence: lens_body`
- `joint: screen_hinge`
- `snapshot intent: reference-matched left view`
- `scope exclusion`

Validation examples:

- `refs --facts + measure`
- `measure hole diameter and centers`
- `align flush on Z + frame`
- `diff major planes`
- `snapshot reference view + user review`
- `external engineering review; TTC cannot verify`

Do not claim that REQ IDs will become stable STEP feature labels.

## Interfaces and positioning

For each interface, state:

- owning part and mating object,
- surface, axis, point, or datum,
- nominal dimensions,
- direction and orientation,
- fit or design clearance,
- motion/DOF and range when applicable,
- validation method.

Write `None for the stated concept scope` when there is no interface requirement.

## Manufacturing intent

Include only geometry-affecting information: process, material intent, stock or
wall thickness, tool/nozzle/bend/draft constraints, hole type, finish allowance,
and user-provided nominal tolerance.

State `Not specified; model is not manufacturing-certified` when not applicable.

## Recommended attachments

List portable filenames already supplied or recommended source documents and
URLs. Mark each as `available`, `link-only`, `recommended`, or `missing-blocker`.
Do not invent a local filename for a document that was not saved.

## Assumptions and delegated choices

List every meaningful proposed default and the reason it does not control fit or
safety. State which choices the user delegated. Avoid burying assumptions inside
feature prose.

## Conflicts and blocking unknowns

For no issues, write:

```text
- None.
```

For a blocker, use an explicit line beginning with:

```text
- BLOCKER: <missing or conflicting controlling evidence and how to clear it>
```

## Limitations

State task-specific capability limits. Typical examples include parameterized
mechanical approximation, unavailable hidden geometry, visual rather than
deterministic appearance review, and external engineering validation needs.

Do not paste generic disclaimers that do not apply.

## Completion check

Before validation, confirm:

- each exact external value has a source,
- each critical/required requirement has a CAD mapping and validation,
- negative requirements are preserved,
- visual estimates are visibly provisional,
- blockers and conflicts match the selected status,
- STEP is primary,
- future TTC paths are relative and same-stem,
- the conditional TTC handoff sections match status.
