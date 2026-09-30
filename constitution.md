# Constitution

These seven principles govern every change. Where a rule elsewhere conflicts, this file wins.

## 1. Specification before implementation

No feature code is written until a human has approved a specification for it.
In practice, this means a pull request that changes `src/` links a spec in `specs/` whose Status is `Approved` and whose approval names a human and a date.

## 2. Simplicity

The simplest solution that meets the approved requirements is the correct one.
In practice, this means no speculative abstractions, optional features, or dependencies beyond what the specification requires.

## 3. Verifiable quality

A change is done only when its behavior is proven by checks anyone can re-run.
In practice, this means every acceptance criterion maps to a test and every validation command in `AGENTS.md` passes before review.

## 4. Security by default

The safe choice is the default and any exception must be explicit and approved.
In practice, this means secrets never enter the repository, inputs are treated as untrusted, and security checks are never weakened to make a change pass.

## 5. Documented decisions

A decision that is not written down did not happen.
In practice, this means approvals, trade-offs, and resolved questions are recorded in the spec, plan, or `docs/open-questions.md`, not only in chat.

## 6. Human control of ambiguity

Humans, not agents, resolve unclear requirements.
In practice, this means an agent that meets missing or conflicting information stops, records the question, and asks a human instead of guessing.

## 7. Focused changes

Each change does one approved thing.
In practice, this means one specification per pull request, no unrelated edits, and no changes outside the approved scope.
