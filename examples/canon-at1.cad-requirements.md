# CAD Requirements Contract

- Contract version: 1
- Status: provisional
- Intent level: concept
- Visual fidelity: reference-fidelity
- TTC suitability: limited
- Suggested basename: canon-at1
- Target: Canon AT-1 exterior assembly with Canon FD 50mm f/1.4 S.S.C. (I) lens and image-specific rear eyecup
- Task type: assembly
- Primary output: STEP
- Secondary outputs: none
- Question rounds used: 0
- Research performed: yes

> Public example note: this task was originally produced with Contract v2. This
> repository copy uses v1 metadata so it can be checked by the current public
> validator; the Visual acceptance section is retained as an additive extension.

## Purpose and scope

Create a parameterized Canon AT-1 exterior assembly that closely matches ten
supplied reference views. Preserve official body and lens envelopes, visible
silhouette, component layout, material boundaries, and identity-critical
features. Treat compound consumer-product surfaces as a controlled mechanical
approximation, not scan-grade surfacing.

Include the exterior body, stepped shoulders, pentaprism housing, hot shoe, top
controls, simplified exterior FD mount surround, rear door, memo holder,
image-specific rear eyecup, strap lugs, and segmented 50mm lens shell. Exclude
film transport, shutter, meter, optical groups, a functional FD bayonet,
threads, working controls, and manufacturing claims.

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User request | user | Canon AT-1 target and delegated dimension research | Current task |
| SRC-002 | ref-01-front.png | image | front silhouette, lens center, prism, controls, material zones | Near-orthographic render |
| SRC-003 | ref-02-rear.png | image | rear silhouette, eyecup, door, memo holder, material zones | Same configuration and scale |
| SRC-004 | ref-03-left.png | image | left depth profile, lens segments, eyecup projection | Near-orthographic side view |
| SRC-005 | ref-04-right.png | image | right depth profile, strap lug, body layers | Near-orthographic side view |
| SRC-006 | ref-05-top.png | image | top silhouette, hot shoe, dials, lever, total depth | Same scale as front view |
| SRC-007 | ref-06-bottom.png | image | bottom plate, circular cover, lens placement | Near-orthographic bottom view |
| SRC-008 | ref-07-front-left.png | image | front-left form hierarchy, transitions, lens segmentation | Perspective review only |
| SRC-009 | ref-08-front-right.png | image | front-right controls, mount surround, material layout | Perspective review only |
| SRC-010 | ref-09-rear-left.png | image | rear-left door, eyecup, top controls | Perspective review only |
| SRC-011 | ref-10-rear-right.png | image | rear-right component hierarchy | Perspective review only |
| SRC-012 | https://global.canon/en/c-museum/product/film96.html | official web | AT-1 identity, 141 x 87 x 48 mm body, FD mount, hot shoe | Canon Camera Museum; accessed 2026-07-31 |
| SRC-013 | https://global.canon/en/c-museum/product/fd150.html | official web | FD 50mm f/1.4 S.S.C. (I) diameter, length, filter size | Canon Camera Museum; accessed 2026-07-31 |

## Research and derivation notes

- Canon specifies the AT-1 body envelope as 141 x 87 x 48 mm. This controls
  body scale and is not inferred from pixels.
- The reference lens marking reads 50mm 1:1.4 S.S.C. The selected interchangeable
  lens is therefore FD 50mm f/1.4 S.S.C. (I), with official envelope diameter
  67 mm, length 49 mm, and filter diameter 55 mm.
- The front body silhouette is approximately 806 px wide. The scale anchor is
  141 mm / 806 px = 0.17494 mm/px. A 502 px front height gives 87.8 mm, consistent
  with the official 87 mm height. Report image-derived values at 1 mm scale.
- The lens-to-eyecup depth silhouette is approximately 662 px, giving
  662 x 0.17494 = 115.8 mm. Use assembly_depth = 116 mm with +/- 3 mm visual
  tolerance.
- The rear eyecup silhouette is approximately 48 x 42 mm with 14 mm projection.
  The memo holder is approximately 53 x 33 mm; use a reversible 2 mm thickness.
- The official AT-1 page lists a 50mm f/1.8 SC standard lens. This is not a body
  conflict because the supplied images show an interchangeable f/1.4 S.S.C. lens.

## Overall geometry and coordinates

- Units: millimeters
- Origin: body bottom-plate center on the bottom plane
- Base plane: XY
- Up axis: +Z
- Axis convention: +Y points toward the lens/front; +X is camera-right when viewed from rear
- Expected body envelope: 141 x 48 x 87 mm from SRC-012
- Expected assembly envelope: approximately 141 x 116 x 88 mm including lens and eyecup
- Primary axes or symmetry: optical axis parallel +Y; main body approximately symmetric about X=0
- Configuration or pose: lens and eyecup installed, rear door closed, controls static

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| body_width | 141 mm | official body X envelope | SRC-012 | official-source | fixed for Canon AT-1 body |
| body_depth | 48 mm | official body Y envelope | SRC-012 | official-source | local protrusion boundaries may be refined |
| body_height | 87 mm | official body Z envelope | SRC-012 | official-source | fixed for Canon AT-1 body |
| assembly_depth | 116 mm nominal | lens front to eyecup rear | SRC-004, SRC-005, SRC-006 | calibrated-image | 113 to 119 mm |
| optical_axis_height | 32 mm nominal | lens axis above bottom plane | SRC-002, SRC-003 | calibrated-image | 30 to 35 mm |
| prism_base_width | 58 mm nominal | front prism base width | SRC-002 | calibrated-image | 55 to 61 mm |
| lower_body_height | 69 mm nominal | rectangular body to shoulder line | SRC-002, SRC-003 | calibrated-image | 67 to 71 mm |
| lens_max_diameter | 67 mm | official lens maximum diameter | SRC-013 | official-source | fixed for selected lens |
| lens_barrel_length | 49 mm | official lens nominal length | SRC-013 | official-source | fixed for selected lens envelope |
| lens_filter_diameter | 55 mm | front filter opening | SRC-013 | official-source | fixed for selected lens |
| eyecup_width | 48 mm nominal | rear eyecup X envelope | SRC-003 | calibrated-image | 46 to 50 mm |
| eyecup_height | 42 mm nominal | rear eyecup Z envelope | SRC-003 | calibrated-image | 40 to 44 mm |
| eyecup_projection | 14 mm nominal | rear eyecup projection along -Y | SRC-004, SRC-005, SRC-006 | calibrated-image | 12 to 16 mm |
| memo_holder_width | 53 mm nominal | rear memo holder width | SRC-003 | calibrated-image | 51 to 55 mm |
| memo_holder_height | 33 mm nominal | rear memo holder height | SRC-003 | calibrated-image | 31 to 35 mm |
| memo_holder_thickness | 2 mm nominal | visual holder thickness | SRC-003 | proposed-default | 1 to 3 mm |
| cosmetic_edge_radius | 2 mm nominal | general exterior edge treatment | SRC-008, SRC-009, SRC-010, SRC-011 | proposed-default | 1 to 3 mm |

## Parts and components

| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
| camera_body_shell | custom approximation | main exterior body and bottom plate | yes | official envelope; local form provisional |
| prism_top_housing | custom approximation | stepped shoulders, compound prism, hot shoe | yes | cross-view-supported; dimensions provisional |
| top_controls | custom approximation | dials, shutter button, advance lever | yes | observed; static visual group |
| front_mount_surround | simplified exterior | visible front ring and faceted surround | yes | non-functional visual geometry |
| lens_body | simplified Canon FD 50mm shell | segmented lens exterior | yes | official envelope plus image segmentation |
| rear_door_memo_holder | custom approximation | closed rear door and memo holder | yes | rear-view-supported; provisional |
| rear_eyecup | image-specific accessory | flared eyecup and view opening | yes | observed; calibrated-image |
| small_controls_and_lugs | custom approximation | strap lugs, small buttons, bottom cover | yes | observed; dimensions provisional |

## Visual acceptance

| ID | Priority | Reference | View | Acceptance target | Target / tolerance | Evidence state | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VIS-001 | critical | SRC-002 | front | complete body, shoulder, and prism silhouette | prism_base_width / body_width = 0.41 +/- 0.03; preserve both shoulder breakpoints | calibrated-image | reference-matched snapshot + user review |
| VIS-002 | critical | SRC-002, SRC-012, SRC-013 | front | lens and mount scale within body | lens_max_diameter / body_width = 0.475 +/- 0.015 | exactly-derived | reference-matched snapshot + user review |
| VIS-003 | critical | SRC-002, SRC-003, SRC-012 | front and rear | optical axis vertical placement | optical_axis_height / body_height = 0.368 +/- 0.025 | calibrated-image | reference-matched snapshot + user review |
| VIS-004 | required | SRC-004, SRC-005 | left and right | body, mount, lens, and eyecup depth segmentation | preserve 48 mm body, 49 mm lens, and 14 mm eyecup profile breakpoints | calibrated-image | reference-matched snapshot + user review |
| VIS-005 | required | SRC-006 | top | lens, body, and eyecup depth silhouette | assembly_depth / body_width = 0.823 +/- 0.025; all centered on optical axis | calibrated-image | reference-matched snapshot + user review |
| VIS-006 | critical | SRC-002, SRC-008, SRC-009 | front and front oblique | compound pentaprism and stepped shoulder identity | use multiple sloped/faceted transitions; do not reduce to one rectangular box | visual-estimate | reference-matched snapshot + user review |
| VIS-007 | required | SRC-002, SRC-006 | front and top | hot shoe, two main dials, shutter button, and advance lever layout | dial center X / body_width approximately -0.36 and +0.35 with +/- 0.03 tolerance | calibrated-image | reference-matched snapshot + user review |
| VIS-008 | required | SRC-003, SRC-010, SRC-011 | rear and rear oblique | eyecup, rear door, and memo holder hierarchy | eyecup 48 x 42 x 14 mm; memo holder 53 x 33 x 2 mm nominal | calibrated-image | reference-matched snapshot + user review |
| VIS-009 | required | SRC-002, SRC-003, SRC-008, SRC-010 | front, rear, and oblique | silver metal, black band, leatherette, rubber, and green glass boundaries | preserve all five visible material zones without dense texture geometry | visual-estimate | reference-matched snapshot + user review |
| VIS-010 | preferred | SRC-008, SRC-009, SRC-010, SRC-011 | opposed oblique | identity details and component layering | preserve strap lugs, segmented lens rings, seams, and major control silhouettes | visual-estimate | reference-matched snapshot + user review |

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | hard | critical | Canon AT-1 body occurrence shall preserve the official envelope | 141 x 48 x 87 mm | SRC-012 | official-source | confirmed | named parameter: body_width, body_depth, body_height | refs --facts + measure body bbox |
| REQ-002 | hard | required | Complete assembly shall preserve the calibrated visual envelope | approximately 141 x 116 x 88 mm; depth +/- 3 mm | SRC-002, SRC-003, SRC-004, SRC-005, SRC-006 | calibrated-image | provisional | assembly occurrence: complete_camera; named parameter: assembly_depth | refs --facts --positioning + measure assembly bbox |
| REQ-003 | functional | required | Lens occurrence shall use the official exterior envelope and share the optical axis | diameter 67 x length 49 mm; filter diameter 55 mm; axis +Y | SRC-013 | official-source | confirmed | assembly occurrence: lens_body; named datum: optical_axis | measure lens envelope + align centered + frame orientation |
| REQ-004 | visual | critical | Exterior form shall satisfy all critical and required silhouette and landmark targets | VIS-001 through VIS-007 | SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-008, SRC-009 | calibrated-image | provisional | snapshot intent: reference-matched orthographic and oblique views | snapshot VIS-001 VIS-002 VIS-003 VIS-004 VIS-005 VIS-006 VIS-007 + user review |
| REQ-005 | visual | required | Rear assembly shall preserve the eyecup, rear door, and memo holder hierarchy | VIS-008 | SRC-003, SRC-010, SRC-011 | calibrated-image | provisional | assembly occurrence: rear_eyecup and rear_door_memo_holder | measure envelopes + snapshot VIS-008 + user review |
| REQ-006 | visual | required | Material boundaries and major identity details shall match the references | VIS-009 and VIS-010 | SRC-002, SRC-003, SRC-008, SRC-009, SRC-010, SRC-011 | visual-estimate | provisional | feature: material zones and identity detail groups | snapshot VIS-009 VIS-010 + user review |
| REQ-007 | negative | critical | Do not model internal film, shutter, meter, optical, or functional FD mount geometry | all excluded | SRC-001 | user-confirmed | confirmed | scope exclusion: exterior bodies only | refs --facts + section snapshot + user review |
| REQ-008 | negative | required | Do not claim real lens fit, accessory fit, manufacturing, or scan-grade reverse engineering | concept exterior only | SRC-001, SRC-012, SRC-013 | proposed-default | provisional | scope exclusion and report limitation | user review of final report |

## Interfaces and positioning

- body_mount_plane: simplified front exterior mounting plane, normal +Y. It only
  positions the visual lens shell and does not define an FD bayonet.
- optical_axis: parallel +Y at X=0 and optical_axis_height = 32 mm nominal.
  Front surround and lens must align centered on this datum.
- rear_viewfinder_frame: rear upper-center datum for the eyecup, facing -Y with
  14 mm nominal projection.
- All controls and doors are static visual components with no functional joints.
- None for real-world fit within the stated concept scope.

## Manufacturing intent

Not specified; model is not manufacturing-certified. Material entries describe
visual zones only and do not imply real grades, wall thickness, assembly method,
surface specification, or tolerance.

## Recommended attachments

- available: ref-01-front.png - front silhouette and landmarks
- available: ref-02-rear.png - rear eyecup, door, and memo holder
- available: ref-03-left.png - left depth profile
- available: ref-04-right.png - right depth profile
- available: ref-05-top.png - top layout and depth silhouette
- available: ref-06-bottom.png - bottom plate and cover details
- available: ref-07-front-left.png - front-left transitions and lens segmentation
- available: ref-08-front-right.png - front-right controls and material zones
- available: ref-09-rear-left.png - rear-left component hierarchy
- available: ref-10-rear-right.png - rear-right component hierarchy
- link-only: https://global.canon/en/c-museum/product/film96.html - official Canon AT-1 body specification
- link-only: https://global.canon/en/c-museum/product/fd150.html - official Canon FD lens specification

## Assumptions and delegated choices

- REQ-002 is provisional and keeps assembly_depth as a replaceable parameter.
- REQ-004 is provisional; VIS-001 through VIS-007 remain pending explicit user approval.
- REQ-005 is provisional; VIS-008 remains pending explicit user approval.
- REQ-006 is provisional; VIS-009 and VIS-010 remain pending explicit user approval.
- REQ-008 is a provisional scope limitation and must be repeated in the final report.
- The supplied images are treated as one same-scale, same-configuration render set.
- The f/1.4 S.S.C. lens and large rear eyecup are image-specific removable components.
- Hidden surfaces, small control dimensions, general radii, lettering, leather texture,
  and knurling remain reversible approximations.

## Conflicts and blocking unknowns

- None for the stated concept and reference-fidelity exterior scope.
- The official standard f/1.8 lens differs from the interchangeable f/1.4 lens shown
  in the images; the image-matched f/1.4 configuration is selected.

## Limitations

- This is a parameterized mechanical approximation from official envelopes and
  rendered views, not original Canon CAD, scan data, or metrology.
- Complex blends and hidden surfaces are TTC-limited and remain provisional.
- Text, fine knurling, leather grain, optical internals, functional controls, and
  real FD interfaces are excluded or simplified.
- A future fit or manufacturing task requires real measurements and interface data.

## TTC CAD brief

CAD brief:
- Model: provisional Canon AT-1 exterior assembly with image-matched FD 50mm f/1.4 S.S.C. lens and rear eyecup
- Visual fidelity: reference-fidelity for silhouette, landmark layout, component hierarchy, and material boundaries; complex surfacing remains limited
- Task type: assembly
- Inputs: `canon-at1.cad-requirements.md`, `canon-at1.handoff.json`, and `ref-01-front.png` through `ref-10-rear-right.png`
- Units: millimeters
- Coordinate convention: origin at body bottom center; XY base; +Z up; +Y lens/front; +X camera-right from rear
- Overall dimensions: official body 141 x 48 x 87 mm; provisional assembly approximately 141 x 116 x 88 mm
- Functional features: labeled body, compound prism/top housing, static controls, simplified mount surround, rear door/memo holder, eyecup, lugs, and segmented lens; exclude internals and functional FD geometry
- Visual acceptance: VIS-001 through VIS-010; stage-gated reference snapshots; all user-review items remain pending until explicit approval
- Manufacturing assumptions: concept exterior only; no real material grade, wall thickness, tolerance, thread, bayonet, optics, or certification
- Positioning/mating: lens and front surround centered on +Y optical_axis; eyecup centered on rear_viewfinder_frame; all parts static
- Paths: `canon-at1.py` generator and `canon-at1.step` primary output in the handoff workspace; same stem
- Validation targets: REQ-001 REQ-002 REQ-003 refs measure align frame; REQ-004 REQ-005 REQ-006 and VIS-001 VIS-002 VIS-003 VIS-004 VIS-005 VIS-006 VIS-007 VIS-008 VIS-009 VIS-010 snapshot user review; REQ-007 refs section snapshot; REQ-008 report user review
- Assumptions: REQ-002 REQ-004 REQ-005 REQ-006 REQ-008 remain provisional; complex surfaces and hidden regions are replaceable approximations

## Copy prompt for TTC

```text
Use $cad.

Run this task from the handoff directory as the user project workspace. Use an
installed $cad skill. Do not run inside, modify, branch, or repair the
earthtojake/text-to-cad source repository. If $cad is unavailable, stop and
report an installation blocker instead of changing the source repository.

Read `canon-at1.handoff.json` and `canon-at1.cad-requirements.md` from disk with
UTF-8 decoding, together with every available attachment in the manifest. Do
not paste or duplicate the complete requirements contract into another message.
Treat the TTC CAD brief as the modeling contract and the Requirements and Visual
acceptance tables as the traceability and acceptance ledgers.

Before coding, plan named parameters, assembly occurrences, features, datums,
and validation targets. Do not re-guess user-confirmed, official-source,
dimensioned-source, or exactly-derived values. Keep every provisional value as
a named, replaceable parameter and report it at handoff.

Use reference-fidelity stage gates. First create a blockout of the official body
envelope, optical axis, lens, eyecup, and major masses. Render the required
reference-matched orthographic views and compare every critical VIS silhouette
and landmark. Refine the smallest responsible source section before adding
secondary controls, seams, material panels, or identity detail. Do not skip a
failed visual stage.

Author build123d Python with gen_step(). Keep `canon-at1.py` and
`canon-at1.step` in this handoff workspace with the same stem. Treat STEP as the
primary validated artifact. Preserve REQ and VIS IDs in planning, source
comments, stable datum/occurrence names, snapshot names, and the final report
where practical.

After generation, run baseline refs --facts --planes --positioning, then the
contract's targeted measure, align, and frame checks. Run and review the full
reference-matched snapshot packet. Visual review cannot override deterministic
envelope or alignment failures.

Do not mark any user-review item passed until the user explicitly approves it.
Until then report it as not verified or pending user review. Repair and rerun
affected checks until deterministic requirements pass or a real blocker is
reported. Finally report every critical and required REQ and VIS item as passed,
failed, or not verified, plus all provisional values, assumptions, exclusions,
and limitations.
```
