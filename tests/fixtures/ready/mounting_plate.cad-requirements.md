# CAD Requirements Contract

- Contract version: 1
- Status: ready
- Intent level: concept
- Suggested basename: mounting_plate
- Target: Dimensioned mounting plate
- Task type: new part
- Primary output: STEP
- Secondary outputs: none
- Question rounds used: 0
- Research performed: not-applicable

## Purpose and scope

Create one fully specified mounting plate without decorative geometry.

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User specification | user | all dimensions and exclusions | Self-contained request |

## Research and derivation notes

External research is not applicable because the geometric contract is complete.

## Overall geometry and coordinates

Millimeters; plate centered on XY; bottom at Z=0; envelope 100 x 60 x 6 mm.

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| plate_length | 100 mm | input envelope | SRC-001 | user-confirmed | fixed nominal value |

## Parts and components

Not applicable: single monolithic part.

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | hard | critical | Plate envelope shall match the supplied dimensions | 100 x 60 x 6 mm | SRC-001 | user-confirmed | confirmed | named parameter: plate envelope | refs --facts + measure |
| REQ-002 | negative | required | No unrequested geometry shall be added | no extra bodies or decoration | SRC-001 | user-confirmed | confirmed | scope exclusion | refs + snapshot + user review |

## Interfaces and positioning

None for the stated concept scope.

## Manufacturing intent

Not specified; model is not manufacturing-certified.

## Recommended attachments

- available: mounting_plate.cad-requirements.md — complete geometric contract

## Assumptions and delegated choices

- Coordinate convention is a non-controlling downstream choice.

## Conflicts and blocking unknowns

- None.

## Limitations

- Validation covers nominal geometry only.

## TTC CAD brief

CAD brief:
- Model: dimensioned mounting plate, single part
- Task type: new part
- Inputs: mounting_plate.cad-requirements.md
- Units: millimeters
- Coordinate convention: centered on XY, bottom at Z=0, +Z up
- Overall dimensions: 100 x 60 x 6 mm from SRC-001
- Functional features: preserve the stated plate and exclude unrequested geometry
- Manufacturing assumptions: nominal geometry only
- Positioning/mating: no mating interface
- Paths: `mounting_plate.py` generator and `mounting_plate.step` primary output in the TTC workspace; same stem
- Validation targets: REQ-001 refs measure; REQ-002 refs snapshot
- Assumptions: coordinate convention does not alter the requested geometry

## Copy prompt for TTC

```text
Use $cad. Read `mounting_plate.cad-requirements.md` completely. Author build123d Python with gen_step(), keep STEP primary, and preserve REQ IDs. Run refs --facts --planes --positioning, measure, and snapshot. Report every requirement as passed, failed, or not verified.
```
