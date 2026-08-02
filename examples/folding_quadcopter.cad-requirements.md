# CAD Requirements Contract

- Contract version: 1
- Status: ready
- Intent level: concept
- Visual fidelity: recognizable
- TTC suitability: suitable
- Suggested basename: folding_quadcopter
- Target: original non-product-specific folding quadcopter mechanism demonstrator
- Task type: assembly
- Primary output: STEP
- Secondary outputs: native GLB, STEP parameter module, animated GIF, PNG review packet
- Question rounds used: 0
- Research performed: yes

> Public example note: this task was originally produced with Contract v2. This
> repository copy uses v1 metadata so it can be checked by the current public
> validator; the Visual acceptance section is retained as an additive extension.

## Purpose and scope

Create an original folding quadcopter assembly whose main purpose is to explain mechanical axes, hierarchy, and motion. Four independent arm branches must fold and unfold one at a time. Each motor and propeller must remain mechanically owned by its arm branch, and each propeller must rotate about its own motor shaft without drift. Add a compact two-axis camera gimbal as a secondary motion mechanism. The result is a concept and presentation model only. Flight performance, aerodynamics, structural safety, electronics, manufacturing, certification, and exact reproduction of any public product are outside scope.

## Sources

| ID | Source | Type | Supports | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | User request | user | Original folding quadcopter, four sequential arms, four coaxial rotating propellers, no drift, optional gimbal, research-only references, no third-party CAD | Confirmed in current task |
| SRC-002 | https://www.dji.com/mavic-3-pro/specs | official web | Folded and unfolded envelope comparison for a public folding quadcopter | Mavic 3 Pro dimensions exclude propellers; accessed 2026-07-31; used only for ratio context |
| SRC-003 | https://dl.djicdn.com/downloads/DJI_Mavic_3/DJI_Mavic_3_User_Manual_v1.4_en.pdf | official web | Front-arm-first deployment sequence followed by rear arms and propeller blades | Mavic 3 manual; accessed 2026-07-31; sequence pattern only |
| SRC-004 | https://www.autelrobotics.com/wp-content/uploads/2024/06/EN_EVO-Nano-Series-Aircraft-User-Manual_V3.0.7.pdf | official web | Compact folded/unfolded ratios and wheelbase context | EVO Nano Series manual; accessed 2026-07-31; dimensions not copied into the design |
| SRC-005 | https://www.autelrobotics.com/wp-content/themes/autel/userfiles/files/2021/10/26/EVO%20II%20User%20Manual.pdf | official web | Front arms deploy before rear arms; rear arms fold before front arms | EVO II manual; accessed 2026-07-31; sequence pattern only |
| SRC-006 | https://www.parrot.com/assets/s3fs-public/2021-01/anafi_usa_product_sheet_white_paper.pdf | official web | Narrow folded topology, opening kinematics, freely mounted compact propeller concept | ANAFI USA white paper; accessed 2026-07-31; visual topology only |
| SRC-007 | https://patents.google.com/patent/US20210214067A1/en | official web | Distal rotor on each arm, hinge housing, coupling pin, coaxial rotation axis, and locking-arm narrative | Public patent publication; accessed 2026-07-31; no claim geometry copied |
| SRC-008 | https://github.com/earthtojake/text-to-cad | official web | STEP-first source, inspection, viewer, and snapshot workflow context | Project referenced by the user; accessed 2026-07-31 |

## Research and derivation notes

- DJI Mavic 3 Pro publishes 231.1 x 98 x 95.4 mm folded and 347.5 x 290.8 x 107.7 mm unfolded, both without propellers. The folded-to-unfolded width ratio is 98 / 290.8 = 0.337 and the length ratio is 231.1 / 347.5 = 0.665. These ratios define context, not copied dimensions.
- Autel EVO Nano publishes 142 x 94 x 62 mm folded and 325 x 260 x 62 mm unfolded. The two in-plane ratios are 142 / 325 = 0.437 and 94 / 260 = 0.362. This supports a compact narrow storage pose at small scale.
- Parrot ANAFI USA publishes 252 x 104 x 84 mm folded and 282 x 373 x 84 mm unfolded. The transverse ratio is 104 / 373 = 0.279. This supports a long-body, narrow-folded topology distinct from the DJI/Autel proportions.
- The manuals agree on front-arm-first deployment and rear-arm-first stowage. The demonstrator adopts that generic sequence while using original pivots, dimensions, housings, and shell geometry.
- The public patent supports a readable chain of body hinge housing -> coupling pin/axis -> arm -> distal rotor and a separate lock narrative. The model uses visible pins, collars, and stop lugs but does not reproduce a patent figure or commercial product.
- Nominal deployed motor vector from each hinge is dx = 86 mm and dy = 71 mm. Arm reach = sqrt(86^2 + 71^2) = 111.521 mm. Deployed arm angle = atan2(71, 86) = 39.54 deg. Fold rotation to a longitudinal storage direction = 180 - 39.54 = 140.46 deg.

## Overall geometry and coordinates

- Units: millimeters
- Origin: center of the fuselage in XY at the arm-hinge reference plane Z = 0
- Base plane: XY
- Up axis: +Z
- Expected envelope: approximately 390 x 285 x 71 mm in the deployed source pose including rigid propeller blades; approximately 220 x 96 x 71 mm at the fully folded viewer pose with blades indexed along X; proposed-default nominal design
- Primary axes or symmetry: +X is nose/front, +Y is left, +Z is up; mirrored left/right geometry with signed hinge rotations
- Configuration or pose: primary STEP is fully deployed; a separate folded key-pose STEP and a looping STEP parameter animation are secondary validation artifacts

## Parameters

| Name | Value / unit | Role | Source | Evidence state | Range / replacement note |
| --- | --- | --- | --- | --- | --- |
| body_length | 184 mm | Main fuselage nominal length | SRC-001 | proposed-default | Reversible concept scale |
| body_width | 72 mm | Main fuselage nominal width | SRC-001 | proposed-default | Reversible concept scale |
| body_height | 30 mm | Main fuselage nominal height | SRC-001 | proposed-default | Reversible concept scale |
| hinge_pivot_x | 64 mm | Absolute front/rear hinge X coordinate | SRC-001 | proposed-default | Mirrored about YZ |
| hinge_pivot_y | 34 mm | Absolute left/right hinge Y coordinate | SRC-001 | proposed-default | Mirrored about XZ |
| deployed_motor_x | 150 mm | Absolute front/rear motor X coordinate | SRC-001 | proposed-default | Mirrored about YZ |
| deployed_motor_y | 105 mm | Absolute left/right motor Y coordinate | SRC-001 | proposed-default | Mirrored about XZ |
| arm_reach | 111.521 mm | Hinge-to-motor center distance | SRC-001 | exactly-derived | sqrt((150 - 64)^2 + (105 - 34)^2) |
| deployed_arm_angle | 39.54 deg | Acute deployed arm angle from +X | SRC-001 | exactly-derived | atan2(71, 86) |
| hinge_fold_angle | 140.46 deg | Magnitude of each storage rotation | SRC-001 | exactly-derived | 180 - deployed_arm_angle |
| arm_width | 14 mm | Arm beam width | SRC-001 | proposed-default | 12 to 18 mm acceptable |
| arm_height | 10 mm | Arm beam height | SRC-001 | proposed-default | 8 to 14 mm acceptable |
| hinge_pin_diameter | 7 mm | Visible mechanical axis diameter | SRC-007 | proposed-default | Concept-only visible pin |
| motor_pod_diameter | 26 mm | Motor and distal pod envelope | SRC-001 | proposed-default | 22 to 32 mm acceptable |
| propeller_radius | 54 mm | Motor-axis to blade-tip radius | SRC-001 | proposed-default | Must avoid source-pose overlap with body |
| gimbal_yaw_limit | +/- 18 deg | Viewer animation yaw range | SRC-001 | proposed-default | Cosmetic mechanism range |
| gimbal_pitch_limit | +/- 10 deg | Viewer animation pitch range | SRC-001 | proposed-default | Cosmetic mechanism range |
| animation_duration | 8 s | Full deployed -> folded -> deployed loop | SRC-001 | proposed-default | 6 to 12 s acceptable |
| animation_fps | 12 fps | Review GIF rate | SRC-001 | proposed-default | 10 to 18 fps acceptable |

## Parts and components

| Part / component | Make or source | Role | Separate body | Evidence / status |
| --- | --- | --- | --- | --- |
| fuselage module | Custom original | Fixed root, battery canopy, belly, landing feet, and gimbal mount | yes | user-confirmed scope; proposed geometry |
| four fixed hinge housings and pins | Custom original | Visible body-side pivot hardware and axis narration | yes | SRC-001, SRC-007; confirmed topology |
| four arm branch modules | Custom original | Independently rotating rigid branches | yes | SRC-001; confirmed |
| four rotating hinge collars | Custom original | Arm-side bearing/collar around each fixed pin | yes | SRC-007; proposed form |
| four motor pod modules | Custom original simplified envelopes | Distal motor body and shaft | yes | SRC-001, SRC-007; confirmed role |
| four propeller modules | Custom original | Hub plus two rigid blades rotating about motor shaft | yes | SRC-001; confirmed |
| two-axis gimbal module | Custom original | Yaw ring, pitch cradle, camera body, and lens | yes | SRC-001; delegated addition |
| hinge stop and lock lugs | Custom original | Explain deployed and folded end-state indexing | yes | SRC-007; proposed form |

## Visual acceptance

| ID | Priority | Reference | View | Acceptance target | Target / tolerance | Evidence state | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VIS-001 | critical | SRC-001, SRC-007 | top | Four readable branch chains and four visible hinge axes | Exactly four body-side axes; each axis owns one arm branch ending in one motor and one propeller | user-confirmed | reference-matched snapshot + user review |
| VIS-002 | required | SRC-001, SRC-003, SRC-005 | animated isometric | Sequential arm motion | Only one arm is in its active fold/unfold interval at a time; stow rear-first and deploy front-first | user-confirmed | reference-matched snapshot + user review |
| VIS-003 | required | SRC-001, SRC-002, SRC-004, SRC-006 | folded top | Compact longitudinal storage silhouette | Folded width including indexed blades <= 0.35 of deployed width; left/right branches remain visibly layered | proposed-default | reference-matched snapshot + user review |
| VIS-004 | critical | SRC-001 | animated isometric | Propeller ownership and coaxial spin | Every propeller stays centered on its own motor through all sampled arm poses; no visual drift or floating | user-confirmed | reference-matched snapshot + user review |
| VIS-005 | required | SRC-001, SRC-007 | close isometric | Mechanical-axis legibility | Fixed pin, rotating collar, arm shoulder, motor shaft, and propeller hub are distinct solids and readable without transparency | visual-estimate | reference-matched snapshot + user review |
| VIS-006 | preferred | SRC-001 | front isometric | Secondary gimbal motion | Nested yaw and pitch axes are distinct, bounded, and return to neutral at loop endpoints | proposed-default | reference-matched snapshot + user review |

## Requirements

| ID | Type | Priority | Requirement | Value / unit | Source | Evidence state | Status | CAD mapping | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | functional | critical | Provide four independently movable arm branches | count = 4 | SRC-001 | user-confirmed | confirmed | assembly occurrences: front_left_branch, front_right_branch, rear_left_branch, rear_right_branch | refs --facts --positioning + snapshot VIS-001 |
| REQ-002 | functional | critical | Animate the four arms one at a time through fold and unfold | sequential non-overlapping intervals | SRC-001 | user-confirmed | confirmed | named parameter: showcase_progress; source feature: four derived hinge fractions | source-review of interval assertions + frame checks at key poses + snapshot VIS-002 |
| REQ-003 | functional | critical | Rotate four propellers about their own motor axes | count = 4; axis = local +Z | SRC-001 | user-confirmed | confirmed | assembly occurrence: propeller_*; named datum: motor_axis_* | refs + frame + source-review of analytical axis report + snapshot VIS-004 |
| REQ-004 | hard | critical | Keep each motor and propeller rigidly owned by its arm branch during arm motion | center drift maximum 0.001 mm in analytical kinematic samples | SRC-001 | user-confirmed | confirmed | assembly occurrence hierarchy: branch_* contains propeller_*; named joint axes | frame on open/folded key-pose occurrences + source-review of analytical transform report + snapshot VIS-004 |
| REQ-005 | visual | required | Make the four arm hinge axes visually explicit | 4 pins, 4 collars, 8 stop/lock lugs | SRC-001, SRC-007 | user-confirmed | confirmed | assembly occurrence: hinge_pin_* and hinge_collar_* | refs --facts + snapshot VIS-005 |
| REQ-006 | functional | required | Use vertical revolute arm axes and constant hinge-to-motor radius | +Z axes; arm reach 111.521 mm | SRC-001 | exactly-derived | derived | joint: arm_hinge_*; named parameter: arm_reach and fold_angle | frame + source-review of analytical distance report |
| REQ-007 | hard | required | Use a fully deployed primary STEP source pose | hinge fraction = 0 for all arms | SRC-001 | proposed-default | confirmed | gen_step() default assembly pose | refs --facts + top/isometric snapshots |
| REQ-008 | functional | preferred | Use rear-first stowage and front-first deployment | RR -> RL -> FR -> FL fold; FL -> FR -> RL -> RR unfold | SRC-003, SRC-005 | proposed-default | confirmed | named parameter: showcase_progress; source feature: interval table | source-review of sequence assertions + frame checks at key poses + snapshot VIS-002 |
| REQ-009 | functional | preferred | Add a nested two-axis camera gimbal | yaw +/- 18 deg; pitch +/- 10 deg | SRC-001 | proposed-default | provisional | assembly occurrence: gimbal_yaw -> gimbal_pitch; named joints: gimbal_yaw_axis and gimbal_pitch_axis | frame + source-review of analytical range report + snapshot VIS-006 |
| REQ-010 | negative | critical | Do not import, download, or embed third-party CAD and do not reproduce a specific product | zero external CAD inputs | SRC-001 | user-confirmed | confirmed | source-only custom build123d geometry; scope exclusion | source-review of generator and handoff manifest |
| REQ-011 | hard | required | Keep STEP as the primary validated artifact and preserve source with the same stem | folding_quadcopter.py and folding_quadcopter.step | SRC-001, SRC-008 | user-confirmed | confirmed | part generator and STEP assembly output paths | refs on generated STEP + source-review of file stem |
| REQ-012 | functional | required | Deliver an interactive motion module and saved motion review | .folding_quadcopter.step.js and animated GIF | SRC-001, SRC-008 | user-confirmed | confirmed | named parameter sidecar and snapshot animation feature | refs on animated STEP source + source-review of sidecar load report + snapshot animated GIF |
| REQ-013 | negative | critical | No motor, hub, blade, collar, or arm may float away from its intended axis or parent branch | no disconnected kinematic transform target | SRC-001 | user-confirmed | confirmed | assembly occurrence hierarchy and named joint datums | refs --positioning + frame + source-review of analytical samples + snapshot VIS-004 |
| REQ-014 | hard | required | The full animation loop returns to the deployed source pose | start and end transform delta <= 1e-6 | SRC-001 | proposed-default | derived | named parameter: showcase_progress; source joint transform functions | source-review of endpoint assertions + frame on generated deployed/folded key poses |
| REQ-015 | visual | required | The folded pose should read as compact and mechanically layered | folded width / deployed width <= 0.35 | SRC-002, SRC-004, SRC-006 | proposed-default | confirmed | assembly placement: folded key pose; named parameter: fold_angle | measure folded/deployed envelopes + snapshot VIS-003 |

## Interfaces and positioning

- The fuselage is the fixed root occurrence. Its arm pivot centers are front_left = (64, 34, 0), front_right = (64, -34, 0), rear_left = (-64, 34, 0), and rear_right = (-64, -34, 0), all with axis +Z.
- Deployed motor centers are front_left = (150, 105), front_right = (150, -105), rear_left = (-150, 105), and rear_right = (-150, -105) in the XY plane. Every hinge-to-motor distance is 111.521 mm.
- Signed fold rotations are front_left +140.46 deg, front_right -140.46 deg, rear_left -140.46 deg, and rear_right +140.46 deg. Fully folded motor centers are approximately (-47.5, 34.0), (-47.5, -34.0), (47.5, 34.0), and (47.5, -34.0) respectively.
- Each arm branch is a nested compound containing its rotating collar, arm beam, motor pod, motor shaft, and propeller module. The propeller spin transform is applied around the source motor center before the branch hinge transform, producing the hierarchical result branch_transform * prop_spin.
- Each propeller axis is coaxial with its motor shaft and remains parallel to +Z because arm folding also uses +Z axes. Validation samples the animation and checks axis origin and arm reach.
- The two-axis gimbal is fixed to the nose belly. The pitch module is nested inside the yaw module. Pitch is applied first around local Y, then yaw around Z, preserving the parent-child relationship.
- The primary STEP is fully deployed. A folded key-pose STEP uses the same geometry constructors, pivots, and signed angles for deterministic envelope inspection.

## Manufacturing intent

- Not specified; model is not manufacturing-certified.
- Housings, clearances, bearings, fasteners, wall thicknesses, wiring, materials, and locking forces are presentation geometry only.

## Recommended attachments

- link-only: https://www.dji.com/mavic-3-pro/specs - public folded/unfolded ratio context
- link-only: https://dl.djicdn.com/downloads/DJI_Mavic_3/DJI_Mavic_3_User_Manual_v1.4_en.pdf - generic deployment sequence
- link-only: https://www.autelrobotics.com/wp-content/uploads/2024/06/EN_EVO-Nano-Series-Aircraft-User-Manual_V3.0.7.pdf - compact ratio and wheelbase context
- link-only: https://www.autelrobotics.com/wp-content/themes/autel/userfiles/files/2021/10/26/EVO%20II%20User%20Manual.pdf - reverse stowage sequence
- link-only: https://www.parrot.com/assets/s3fs-public/2021-01/anafi_usa_product_sheet_white_paper.pdf - narrow folded topology and opening kinematics
- link-only: https://patents.google.com/patent/US20210214067A1/en - hinge/pin/lock mechanical narrative
- link-only: https://github.com/earthtojake/text-to-cad - STEP-first workflow context

## Assumptions and delegated choices

- Overall scale, body surfacing, colors, arm section, motor envelope, propeller blade profile, hinge-lug form, and gimbal shape are reversible proposed defaults because the user explicitly delegated design decisions and requested an original concept.
- Public product dimensions are used only as ratio evidence. No public product dimension set, silhouette, branding, surface, or part layout is copied.
- Rigid two-blade propellers are used so motor-axis rotation remains legible. Blade-folding is not required because the two-axis gimbal already provides a secondary mechanism.
- REQ-009 is a provisional cosmetic mechanism choice: the two-axis gimbal geometry and +/- 18 deg yaw, +/- 10 deg pitch ranges are replaceable and do not control any flight, fit, or safety claim.
- Propellers index along world X during the folded hold to preserve a compact top-view silhouette. They complete integer turns before and after the arm sequence so the loop closes exactly.
- The viewer sidecar owns presentation-time motion. STEP remains static BREP geometry; the folded key-pose STEP and analytical report validate representative kinematic states.
- Cosmetic fillets and chamfers may be reduced or omitted if they threaten robust BREP generation, provided the silhouette and mechanical hierarchy remain recognizable.

## Conflicts and blocking unknowns

- None.

## Limitations

- The design is not intended to fly and does not model aerodynamic loads, center of gravity, motor performance, wiring, electronics, or propeller clearance under thrust.
- The STEP parameter animation applies viewer-time rigid transforms; it is not a persistent STEP kinematic constraint system.
- Collision review is visual and analytical for the authored presentation poses, not a complete swept-volume or contact simulation.
- VIS items remain pending user review until the user explicitly approves the saved snapshots and GIF.

## TTC CAD brief

CAD brief:
- Model: original folding quadcopter mechanism demonstrator with recognizable mechanical hierarchy
- Visual fidelity: recognizable; original faceted industrial design with visible axes, collars, motor shafts, and nested mechanisms rather than any product match
- Task type: new assembly
- Inputs: `folding_quadcopter.cad-requirements.md`, `folding_quadcopter.handoff.json`, and link-only public sources
- Units: millimeters
- Coordinate convention: fuselage XY center at arm-hinge reference plane Z = 0; +X front, +Y left, +Z up
- Overall dimensions: nominal deployed envelope about 390 x 285 x 71 mm including blades; folded viewer/key-pose envelope about 220 x 96 x 71 mm; proposed-default concept scale
- Functional features: fixed fuselage, four vertical hinge pins/housings, four nested arm branches, four distal motor pods and coaxial rigid propellers, stop/lock lugs, and nested two-axis gimbal; no imported CAD
- Visual acceptance: VIS-001 through VIS-006; top, isometric, folded, and animated reviews; user-review gate remains pending
- Manufacturing assumptions: presentation geometry only; no flight, structural, fit, or manufacturing claim
- Positioning/mating: four pivots at (+/- 64, +/- 34, 0), motor centers at (+/- 150, +/- 105), reach 111.521 mm, signed fold angles +/- 140.46 deg, prop modules nested under branches, pitch nested under yaw
- Paths: `folding_quadcopter.py` generator and `folding_quadcopter.step` primary output in the handoff workspace; same stem
- Validation targets: REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-014, and REQ-015; VIS-001, VIS-002, VIS-003, VIS-004, VIS-005, and VIS-006; refs --facts --planes --positioning, frame, measure, source-review, snapshot PNG/GIF, and user review
- Assumptions: REQ-009 is a replaceable cosmetic two-axis gimbal; other choices are reversible original proportions and styling, a static deployed STEP plus folded key pose and viewer-time animation, rigid propeller blades, and no third-party CAD

## Copy prompt for TTC

```text
Use $cad.

Run this task from the handoff directory as the user project workspace. Use an
installed $cad skill. Do not run inside, modify, branch, or repair the
earthtojake/text-to-cad source repository. If $cad is unavailable, stop and
report an installation blocker instead of changing the source repository.

Read `folding_quadcopter.handoff.json` and
`folding_quadcopter.cad-requirements.md` from disk with UTF-8 decoding,
together with every available attachment in the manifest. Do not paste or
duplicate the complete requirements contract into another message. Treat the
TTC CAD brief as the modeling contract and the Requirements and Visual
acceptance tables as the traceability and acceptance ledgers.

Before coding, plan named parameters, parts/features, datums/positioning, and
validation targets. Do not re-guess user-confirmed, official-source,
dimensioned-source, or exactly-derived values. Keep every provisional value as
a named, replaceable parameter and report it at handoff.

Author build123d Python with gen_step(). Keep `folding_quadcopter.py` and
`folding_quadcopter.step` in this handoff workspace with the same stem. Treat
STEP as the primary validated artifact. Preserve REQ and VIS IDs in planning,
source comments, stable datum/occurrence names, and the final report where
practical. Create an original labeled assembly hierarchy, a folded key-pose
STEP, a native GLB sidecar, and a same-stem STEP parameter module that animates
the four arm hinges sequentially, the four propellers coaxially, and the nested
two-axis gimbal. Generate and review an animated GIF.

After generation, run baseline refs --facts --planes --positioning, then the
contract's targeted measure, align, frame, analytical motion, and envelope
checks. Run and review the required snapshot packet. Visual review cannot
override deterministic failures. Repair and rerun affected checks until every
deterministic critical and required item passes or a real blocker is reported.

Do not mark any user-review item passed until the user explicitly approves it.
Until then report it as not verified or pending user review. Finally report
every critical and required REQ and VIS item as passed, failed, or not verified,
plus all provisional values, assumptions, external review items, and limits.
```
