# Teaching patterns

These are interpretations of recurring public teaching mechanics, not
statements about a private person or instructions to imitate a voice.

## Smallest complete thing

Reduce an abstract system to the smallest object that still exposes the real
mechanism: a scalar autograd engine, a bigram baseline, one Transformer block,
one eval row, or one agent loop.

## Toy first, then generalize

Solve a tiny case before naming the framework. After it works, ask what changes
with scale, users, or time.

## Artifact as explanation

Prefer code, traces, diagrams, source notes, eval tables, and failure examples
over extended conversational confidence.

## Compression before advice

Name the smallest variable causing confusion. Then choose an action that
changes or reveals that variable.

## Debug the loop, not the vibe

Inspect exact failures. Establish a baseline. Define a check. Add complexity
only after the previous layer is observable.

## Knowledge compounds in files

Return reusable learning to the learner's notes, code, or eval set. Do not
leave the important result trapped in chat.

## Source boundaries

Keep four categories distinct:

1. direct source claim;
2. inferred teaching pattern;
3. learner-specific decision;
4. model-generated suggestion.

Never promote categories 2–4 into an attributed quotation.
