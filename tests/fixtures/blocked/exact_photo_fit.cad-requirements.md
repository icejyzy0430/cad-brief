# CAD Requirements Contract

- Contract version: 1
- Status: blocked
- Intent level: fit
- Suggested basename: exact_photo_fit
- Target: Unknown pictured product requiring exact accessory fit
- Task type: new part
- Primary output: STEP
- Secondary outputs: none
- Question rounds used: 2
- Research performed: unavailable

## Purpose and scope

The requested exact-fit model cannot be handed to TTC without interface evidence.

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User request and image | image | visual target and exact-fit intent | No scale or hidden interface view |

## Research and derivation notes

No dimensioned source or reliable product identity is available.

## Overall geometry and coordinates

Scale and controlling datum remain unknown.

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| interface_width | unknown | controlling fit input | SRC-001 | unknown | requires dimensioned interface evidence |

## Parts and components

| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
| target body | unknown product | mating object | yes | identity unknown |

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | hard | critical | The accessory interface must fit the real product | unknown | SRC-001 | unknown | unknown | named datum: missing interface | external review: dimensioned interface required; TTC cannot verify |

## Interfaces and positioning

REQ-001 dimensions, axis, and mating datum are unknown.

## Manufacturing intent

Exact physical fit is requested, but manufacturing geometry is blocked.

## Recommended attachments

- missing-blocker: dimensioned interface drawing or exact product STEP — required for REQ-001

## Assumptions and delegated choices

- No approximation is authorized for REQ-001.

## Conflicts and blocking unknowns

- BLOCKER: REQ-001 lacks target identity, scale, and controlling interface dimensions.

## Limitations

- A photograph cannot establish the requested exact fit.

## TTC handoff withheld

No `$cad` launch prompt was generated because the requested fit depends on the blocker above.
