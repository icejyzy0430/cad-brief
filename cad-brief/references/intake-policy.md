# Intake policy

Use this policy to extract the user's existing information and spend no more than
two question rounds on the decisions that only the user can make.

## Contents

- [Count question rounds](#count-question-rounds)
- [Extract before asking](#extract-before-asking)
- [Rank missing information](#rank-missing-information)
- [Round one](#round-one)
- [Round two](#round-two)
- [After round two](#after-round-two)
- [Task playbooks](#task-playbooks)
- [Stop conditions](#stop-conditions)

## Count question rounds

A question round is one assistant message that asks the user to reply. Count it
even if the message contains multiple choices or short subquestions.

Do not count:

- a progress update that needs no reply,
- research performed without user input,
- the final requirements summary,
- a warning that does not ask for a decision.

Maintain `question_rounds_used` internally and write its final value into the
requirements package. Valid values are `0`, `1`, and `2`.

## Extract before asking

Read the full request and all accessible attachments first. Build an internal
inventory:

| Category | Extract |
| --- | --- |
| Target | object category, brand, series, candidate model, variant |
| Purpose | visual concept, fit, manufacturing intent, engineering review |
| Scale | dimensions, units, known objects, drawing callouts |
| Geometry | envelope, parts, features, symmetry, hidden regions |
| Interfaces | mating objects, mounting faces, axes, holes, connectors, motion |
| Constraints | must-have, must-not-have, immutable details, output formats |
| Freedom | choices delegated to the agent |
| Evidence | text, image, drawing, datasheet, STEP, measurement, URL |

Never ask the user to repeat extracted information.

## Rank missing information

Ask only when the answer has high information gain. Rank candidates in this
order:

1. A choice that changes whether the task is concept, fit, manufacture, or
   engineering review.
2. Exact target identity or variant when variants have different geometry.
3. A controlling interface or mating object unavailable from public research.
4. A user-specific success criterion or immutable feature.
5. A conflict between authoritative sources that only the user can resolve.

Do not spend a question on:

- units when millimeters can be declared as an assumption,
- coordinate origin or up axis,
- cosmetic fillet or chamfer values,
- publicly documented product dimensions,
- public standards and common hardware data,
- decorative choices the user has delegated,
- exact hidden geometry for a concept task when it can be openly approximated.

## Round one

Use round one for user-only context. Ask no more than three tightly related
items in one compact message. Provide a recommended interpretation when useful.

Default pattern:

```text
Before I prepare the CAD brief, please confirm:
1. Is this for visual resemblance, real-world fit, or manufacturing?
2. What exact model/variant is it, or may I identify candidates from the images?
3. Which dimensions, mating objects, or visible details must not change?
```

Adapt this pattern instead of asking all three mechanically. If the request
already answers an item, omit it.

After receiving the response, research before asking anything else.

## Round two

Use round two only after research. Present a small decision set with effects.

Good uses:

- choose among two or three plausible product variants,
- resolve conflicting official dimension boundaries,
- choose exact-fit versus provisional-concept scope,
- accept or reject a named approximation that materially affects topology.

Example:

```text
The images match Sony FX3 and FX30 most closely. Their bodies are similar, but
the sensor marking and some control details differ.

Choose FX3 or FX30. If neither can be confirmed, I recommend a provisional FX3
exterior model that does not claim accessory fit.
```

Bad uses:

- asking the user to fill a long CAD questionnaire,
- asking for ten dimensions that public documents contain,
- asking for cosmetic radii one by one,
- repeating round-one questions,
- requesting another answer after the second round.

## After round two

Do not ask again. Resolve every remaining item as one of:

- researchable fact,
- exact derivation,
- low-risk proposed default,
- provisional visual estimate,
- explicit unknown,
- source conflict,
- blocker.

Then apply the readiness gates. A blocker is a valid outcome; do not hide it by
inventing a number.

## Task playbooks

### Fully dimensioned simple part

- Ask zero questions.
- Do not research unrelated material or manufacturing data.
- Preserve every positive and negative requirement.
- Produce `ready` unless the supplied dimensions conflict.

### Vague generic part

- Ask whether the goal is concept or real fit.
- Ask for the mating object only if fit is intended.
- Use named, editable defaults for concept geometry.

### Named real product with images

- Ask for exact model or permission to identify it.
- Research official sources and variants.
- Use round two only when identification remains ambiguous.
- Default to `provisional` for unsupported complex surfaces or hidden geometry.

### Assembly or enclosure

- Prioritize purchased-part identities, interface geometry, fixed root, part
  boundaries, motion, and clearance.
- Prefer existing STEP or dimensioned drawings over manual transcription.
- Do not claim fit-ready when a controlling interface is absent.

### Manufacturing-sensitive part

- Ask only for user-specific process, material, machine, environment, and fit
  choices that change geometry.
- Research public process or hardware standards when appropriate.
- Keep certification and process approval outside TTC.

### Safety or compliance request

- Classify as `engineering-review`.
- Capture load cases, environment, standards, analysis, testing, and sign-off as
  external requirements.
- Do not let a plausible CAD shape become a safety claim.

## Stop conditions

Stop asking when any is true:

- all intent-level blockers are resolved,
- remaining unknowns affect only delegated or cosmetic choices,
- the user accepts a provisional concept,
- two question rounds have been used,
- the task must be blocked honestly.
