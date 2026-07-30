# CAD Requirements Contract

- Contract version: 1
- Status: <ready | provisional | blocked>
- Intent level: <concept | fit | manufacturing-intent | engineering-review>
- Suggested basename: <safe_basename>
- Target: <object and model or variant>
- Task type: <new part | assembly | modification>
- Primary output: STEP
- Secondary outputs: <none or requested formats>
- Question rounds used: <0 | 1 | 2>
- Research performed: <yes | not-applicable | unavailable>

## Purpose and scope

<What is being modeled, why, what success means, and what is outside scope.>

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User request | user | <purpose and user-confirmed requirements> | <task-local note> |
| SRC-002 | <filename or direct URL> | <image/drawing/CAD/official web/datasheet/standard/review> | <specific supported facts> | <variant, boundary, date, or limitation> |

## Research and derivation notes

- <Only research decisions or derivations that affect requirements/readiness.>
- <For a derivation, cite inputs, method, units, result, and rounding.>

## Overall geometry and coordinates

- Units: <explicit or assumed>
- Origin: <functional origin or proposed default>
- Base plane: <for example XY>
- Up axis: <for example +Z>
- Expected envelope: <dimensions, boundary, source/evidence state>
- Primary axes or symmetry: <description>
- Configuration or pose: <folded/deployed/neutral/etc.>

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| <parameter_name> | <value> | <input or derived role> | <SRC-###> | <allowed evidence state> | <range or replacement evidence> |

## Parts and components

| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
| <name> | <custom, purchased identity, or source> | <function> | <yes/no> | <confirmed/provisional/etc.> |

<!-- For a monolithic part, replace the table with: Not applicable: single monolithic part. -->

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | <hard/functional/visual/negative/manufacturing> | <critical/required/preferred> | <normative requirement> | <value, range, enum, or description> | <SRC-###> | <allowed evidence state> | <confirmed/derived/provisional/unknown/conflict> | <named parameter/feature/datum/joint/occurrence/snapshot intent/exclusion> | <real TTC check, user review, or external review> |

## Interfaces and positioning

- <Owning part and mating object; datum/surface/axis; direction; dimensions;
  clearance; motion; validation.>

<!-- If none: None for the stated concept scope. -->

## Manufacturing intent

- <Only geometry-affecting process, material, thickness, tool/nozzle/bend/draft,
  hole intent, and supplied nominal tolerance.>

<!-- If unspecified: Not specified; model is not manufacturing-certified. -->

## Recommended attachments

- <available | link-only | recommended | missing-blocker>: <portable filename or direct URL> — <why TTC needs it>

## Assumptions and delegated choices

- <Explicit reversible assumption, evidence state, and why it does not control an unsupported claim.>
- <Choice the user delegated to the downstream CAD agent.>

## Conflicts and blocking unknowns

- None.

<!-- For blocked work use one or more: - BLOCKER: <issue and evidence needed to clear it> -->

## Limitations

- <Task-specific limitations; omit generic irrelevant disclaimers.>

<!-- READY/PROVISIONAL ONLY: retain the next two sections. -->

## TTC CAD brief

CAD brief:
- Model: <part or assembly name and intended fidelity>
- Task type: <new part, assembly, or modification>
- Inputs: <<safe_basename>.cad-requirements.md and portable attachment filenames/URLs>
- Units: <explicit or assumed>
- Coordinate convention: <origin, base plane, up axis>
- Overall dimensions: <envelope and important evidence states>
- Functional features: <parts, features, counts, dimensions, and negative constraints>
- Manufacturing assumptions: <geometry-affecting assumptions and scope limits>
- Positioning/mating: <interfaces, datums, placements, joints, and alignment rules>
- Paths: `<safe_basename>.py` generator and `<safe_basename>.step` primary output in the TTC workspace; same stem
- Validation targets: <REQ IDs mapped to refs/measure/align/frame/diff/snapshot/user/external review>
- Assumptions: <provisional choices, exclusions, and unresolved non-blockers>

## Copy prompt for TTC

```text
Use $cad.

Read `<safe_basename>.cad-requirements.md` completely, together with the
available attachments listed in Recommended attachments. Treat its `TTC CAD
brief` as the modeling contract and retain the Requirements table as the
traceability and acceptance ledger.

Before coding, make a concise plan of named parameters, parts/features,
datums/positioning, and validation targets. Do not re-guess `user-confirmed`,
`official-source`, `dimensioned-source`, or `exactly-derived` values. Make every
provisional dimension a named, replaceable parameter and report it at handoff.
Do not silently resolve a confirmed conflict or missing controlling interface.

Author build123d Python with `gen_step()`. Keep `<safe_basename>.py` and
`<safe_basename>.step` in the TTC workspace with the same stem. Treat STEP as
the primary validated artifact; create secondary mesh outputs only when
requested.

Preserve REQ IDs in source comments, planning, stable datum/occurrence names,
and the final validation report where practical. Do not claim that every REQ ID
is a stable STEP feature label.

After generation, run the baseline `refs --facts --planes --positioning`, then
the contract's targeted `measure`, `align`, `frame`, or `diff` checks. Run and
review the mandatory snapshot packet, including specified reference-matched or
section views. Visual review cannot override deterministic failures.

Repair the smallest responsible source section and rerun affected checks until
the contract passes or a real blocker is reported. Finally report every
critical and required REQ as passed, failed, or not verified, plus all
provisional values, assumptions, external-review items, and limitations.
```

<!-- BLOCKED ONLY: delete TTC CAD brief and Copy prompt for TTC, then use: -->

<!--
## TTC handoff withheld

No `$cad` launch prompt was generated because the requested intent depends on
the blockers listed above. Clear those blockers or explicitly accept a
provisional concept scope before geometry generation.
-->
