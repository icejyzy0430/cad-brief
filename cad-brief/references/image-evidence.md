# Image evidence

Use this reference whenever photographs, screenshots, scans, renders, or
undimensioned drawings contribute to the requirements.

## Contents

- [Fundamental limit](#fundamental-limit)
- [Inspect all images first](#inspect-all-images-first)
- [Build a visual inventory](#build-a-visual-inventory)
- [Establish scale](#establish-scale)
- [Cross-view reasoning](#cross-view-reasoning)
- [Hidden geometry](#hidden-geometry)
- [Complex surfaces](#complex-surfaces)
- [Visual validation target](#visual-validation-target)
- [Image-driven readiness](#image-driven-readiness)

## Fundamental limit

An unscaled image is design intent, not an engineering specification. It may
support identity, visible topology, component presence, silhouette, proportions,
material regions, and style. It does not by itself establish exact size, depth,
wall thickness, hole depth, hidden geometry, or fit.

## Inspect all images first

For each image, record:

- source ID and filename or URL,
- likely view direction,
- perspective strength and lens distortion,
- visible faces and occluded regions,
- possible scale references,
- whether it shows the same model/variant and configuration as other images,
- whether accessories alter the visible envelope.

Do not ask for information that another supplied view already reveals.

## Build a visual inventory

Decompose the target at three levels:

- macro: main body, separate parts, overall silhouette, major axes,
- meso: handles, panels, bosses, feet, mounts, screens, doors, vents,
- micro: buttons, screws, seams, labels, small chamfers, surface texture.

For every item, classify it as:

- `observed`: directly visible in one or more suitable views,
- `cross-view-supported`: consistent across multiple views,
- `inferred`: plausible but not directly visible,
- `unknown`: evidence does not support a choice,
- `excluded`: deliberately outside the requested model scope.

Map observed items that matter to identity or function into requirements. Do not
turn every decorative pixel into a CAD feature.

## Establish scale

Use scale in this order:

1. dimension callout in a suitable drawing,
2. user-confirmed dimension,
3. official overall dimension for the exact model and configuration,
4. known object that is coplanar and not badly perspective-distorted,
5. no scale.

When no scale exists:

- for `concept`, choose a documented nominal envelope and mark it provisional;
- for `fit`, seek a dimensioned source or return blocked;
- never report pixel-derived millimeters as exact.

When scaling from an image, preserve realistic precision. State the anchor,
image plane, ratio, perspective limitation, and rounding.

## Cross-view reasoning

Use multiple views to constrain different axes. Confirm that:

- the views depict the same variant and accessory state,
- front/top/side labels or orientations are not assumed incorrectly,
- repeated features have consistent count and placement,
- the estimated depth is supported by a non-coplanar view,
- symmetric geometry is actually symmetric rather than visually foreshortened.

If two views disagree, inspect cropping, perspective, deployment state, and
variant identity before recording a source conflict.

## Hidden geometry

Never invent hidden or internal structures as facts. Choose one action:

- find a section, bottom view, teardown, service document, patent, or CAD source;
- represent only a documented envelope;
- create a reversible provisional construction and label it;
- exclude the hidden region from scope;
- block exact fit or reproduction when the hidden geometry controls it.

For ordinary product photography, shell thickness, internal ribs, fastener
engagement, connector depth, and sealing features are normally unknown.

## Complex surfaces

Treat consumer-product curvature as a parameterized mechanical approximation
unless scan data, surface sections, or original CAD is available. Identify:

- silhouette-critical curves,
- functional planar and cylindrical interfaces,
- tangent transitions and major blends,
- curves that can be simplified without changing purpose,
- decorative textures that should not become B-Rep geometry.

Do not promise scan-grade, Class-A, or original-manufacturer surface fidelity
from photographs alone.

## Visual validation target

For reproduction tasks, specify snapshot views that correspond to useful
references:

- one reference-matched viewpoint,
- an opposed isometric view for hidden-face sanity,
- orthographic top/front/side views when silhouette or layout matters,
- a section view when a documented cavity or shell must be checked.

Snapshot review supports visual requirements and user review. It cannot replace
deterministic checks for sourced dimensions and interfaces.

## Image-driven readiness

An image-led task may be:

- `ready` only when its controlling geometry is supported by dimensioned or
  otherwise authoritative evidence,
- `provisional` when a clearly parameterized visual approximation is useful,
- `blocked` when the user requires exact hidden geometry, fit, or manufacture
  that the images cannot support.
