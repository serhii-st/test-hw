# Contributing

Follow these steps in order. Rules and conventions: [AGENTS.md](AGENTS.md),
[constitution.md](constitution.md), [docs/standards.md](docs/standards.md).

## 1. Write and approve a specification

1. Copy [specs/TEMPLATE.md](specs/TEMPLATE.md) to `specs/NNNN-short-name.md` (next free number).
2. Fill every section. Set `Status: Draft`. Agents may use the
   [spec-generator](skills/spec-generator/SKILL.md) skill.
3. List every unknown under **Open Questions**. Do not guess answers.
4. Set `Status: In Review` and ask a human reviewer. (Agents may set `Draft` and
   `In Review`; only a human sets `Approved` or `Rejected`.)
5. An approved reviewer listed in [AGENTS.md](AGENTS.md#approved-human-reviewers)
   resolves open questions and sets `Status: Approved` (or `Rejected`),
   writing their name and date under **Human approval**.
6. An agent cannot approve its own specification, or any specification.

## 2. Create a plan and tasks

1. Only for a spec with `Status: Approved`.
2. Copy [plans/TEMPLATE.md](plans/TEMPLATE.md) to `plans/NNNN-short-name.md` (same number as the spec).
3. Copy [tasks/TEMPLATE.md](tasks/TEMPLATE.md) to `tasks/NNNN-short-name.md`.
4. Every task must trace to a requirement ID (for example `R1`).
5. Use the [test-plan-generator](skills/test-plan-generator/SKILL.md) skill to map
   acceptance criteria to tests.

## 3. Implement and test approved scope

1. Work on a branch named per [docs/standards.md](docs/standards.md).
2. Write `unittest` tests first for each acceptance criterion, in `tests/test_<module>.py`.
3. Implement only what the tasks list, in `src/`.
4. If scope must change, stop, update the spec, and get re-approval.

## 4. Validate and submit a change

1. Run every command in [AGENTS.md § Validation commands](AGENTS.md#validation-commands).
2. Fix failures. Never weaken a test or check to pass.
3. Copy [review/change-template.md](review/change-template.md) into the pull request
   description and answer every item with Yes, No, or Not applicable plus evidence.
4. Open the pull request. Reviewers (or the [pr-reviewer](skills/pr-reviewer/SKILL.md)
   skill) use the same checklist.
5. A human merges. Any `No` answer blocks merge unless a human records an exception.
