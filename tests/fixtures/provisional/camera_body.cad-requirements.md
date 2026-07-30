# CAD Requirements Contract

- Contract version: 1
- Status: provisional
- Intent level: concept
- Suggested basename: camera_body
- Target: Camera body exterior approximation
- Task type: new part
- Primary output: STEP
- Secondary outputs: GLB
- Question rounds used: 2
- Research performed: yes

## Purpose and scope

Create a recognizable parameterized exterior without claiming accessory fit.

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | camera-front.png | image | visible silhouette and controls | Unscaled reference image |
| SRC-002 | https://example.com/official-spec | official web | body envelope | Test-only public-source placeholder |

## Research and derivation notes

The published envelope controls scale; grip curvature remains a visual estimate.

## Overall geometry and coordinates

Millimeters; centered body frame; published envelope; neutral screen pose.

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| body_width | 130 mm | envelope input | SRC-002 | official-source | replace if variant changes |
| grip_radius | 28 mm nominal | visual profile | SRC-001 | visual-estimate | adjustable parameter |

## Parts and components

| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
| camera body | custom approximation | exterior shell | no | provisional |

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | hard | critical | Overall body envelope shall use the published nominal dimensions | 130 x 85 x 80 mm | SRC-002 | official-source | confirmed | named parameter: body envelope | refs --facts + measure |
| REQ-002 | visual | required | Grip silhouette shall resemble the supplied view | adjustable profile | SRC-001 | visual-estimate | provisional | snapshot intent: reference-matched front view | snapshot + user review |

## Interfaces and positioning

None for the accepted concept scope; accessory fit is excluded.

## Manufacturing intent

Not specified; model is not manufacturing-certified.

## Recommended attachments

- available: camera-front.png — reference-matched snapshot view
- link-only: https://example.com/official-spec — envelope source

## Assumptions and delegated choices

- REQ-002 is a visual approximation and must remain a named, replaceable parameter.

## Conflicts and blocking unknowns

- None for the accepted concept scope.

## Limitations

- Hidden surfaces and complex blends are approximate; no physical fit is claimed.

## TTC CAD brief

CAD brief:
- Model: provisional camera body exterior approximation
- Task type: new part
- Inputs: camera_body.cad-requirements.md and camera-front.png
- Units: millimeters
- Coordinate convention: body-centered origin, XY base plane, +Z up
- Overall dimensions: 130 x 85 x 80 mm from SRC-002
- Functional features: recognizable body and grip without undocumented internals
- Manufacturing assumptions: concept geometry only
- Positioning/mating: accessory interfaces excluded
- Paths: `camera_body.py` generator and `camera_body.step` primary output in the TTC workspace; same stem
- Validation targets: REQ-001 refs measure; REQ-002 snapshot user review
- Assumptions: REQ-002 grip profile is provisional and adjustable

## Copy prompt for TTC

```text
Use $cad. Read `camera_body.cad-requirements.md` completely. This handoff is provisional. Author build123d Python with gen_step(), keep STEP primary, and preserve REQ IDs. Run refs --facts --planes --positioning, measure, and snapshot. Report every requirement as passed, failed, or not verified.
```
