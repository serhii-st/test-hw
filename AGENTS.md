# AGENTS.md

Canonical instructions for any AI agent or human working in this repository.
These rules are platform-neutral. Tool-specific files (if any) must only point here.

## Project purpose

AI-Ready Project Foundation: the engineering and AI-collaboration base for a generic
Python project. It contains governance, templates, validation, and reusable skills only.
Features are defined only by approved specifications in `specs/`.

- Language: Python 3.10 or newer.
- Test runner: `unittest` (standard library).
- CI: none. Validation runs locally.
- License: none.

Decisions: [docs/open-questions.md](docs/open-questions.md).

## Folder map

| Path | Contents |
|------|----------|
| `AGENTS.md` | This file. Entry point for agents. |
| `README.md` | Human overview. |
| `CONTRIBUTING.md` | How to propose, build, validate, and submit a change. |
| `constitution.md` | Seven governing principles. |
| `docs/` | Standards and open questions. |
| `specs/` | Specifications. `TEMPLATE.md` is the starting point. |
| `plans/` | Implementation plans. `TEMPLATE.md` is the starting point. |
| `tasks/` | Task lists. `TEMPLATE.md` is the starting point. |
| `skills/<name>/SKILL.md` | Reusable AI skills. |
| `skill-runs/<name>.md` | One recorded run per skill. |
| `review/` | Change review checklist. |
| `scripts/` | Validation tooling (standard library only). |
| `src/` | Application code. Empty until a specification is approved. |
| `tests/` | Tests. Empty until a specification is approved. |

## Governance documents

- [constitution.md](constitution.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/standards.md](docs/standards.md)
- [docs/open-questions.md](docs/open-questions.md)
- [specs/TEMPLATE.md](specs/TEMPLATE.md)
- [plans/TEMPLATE.md](plans/TEMPLATE.md)
- [tasks/TEMPLATE.md](tasks/TEMPLATE.md)
- [review/change-template.md](review/change-template.md)
- Skills: [spec-generator](skills/spec-generator/SKILL.md),
  [pr-reviewer](skills/pr-reviewer/SKILL.md),
  [test-plan-generator](skills/test-plan-generator/SKILL.md)
- Skill runs: [spec-generator](skill-runs/spec-generator.md),
  [pr-reviewer](skill-runs/pr-reviewer.md),
  [test-plan-generator](skill-runs/test-plan-generator.md)

## Workflow

request → specification → human approval → plan → tasks → implementation → validation → review

Details: [CONTRIBUTING.md](CONTRIBUTING.md).

## Validation commands

Run from the repository root. Requires Python 3.10 or newer and no third-party packages.

1. Always run:

   ```bash
   python scripts/validate.py
   ```

   Pass: the last line is `VALIDATION PASSED` and the exit code is `0`.

2. Does `tests/` contain any `test_*.py` file? If Yes, also run:

   ```bash
   python -m unittest discover -s tests -v
   ```

   Pass: the last line is `OK` and the exit code is `0`.

## Required rules

Each rule is answered Yes or No. Every answer must be Yes before submitting.

1. Is every feature change backed by a specification with Status `Approved` and a human name and date? (No feature implementation without an approved specification.)
2. Did you run all applicable validation commands and did they pass before submitting?
3. Are secrets absent from code, docs, logs, commits, and outputs?
4. Are security controls and tests unchanged or strengthened (never weakened, skipped, or deleted to pass)?
5. Are protected paths unchanged, or is explicit human approval recorded for each change?
6. When a requirement was unclear, did you stop and ask instead of guessing?
7. Did an approved human reviewer (listed below), not an agent, approve the specification?

## Approved human reviewers

Only these people may set a spec to `Approved` or `Rejected`, or approve protected-path changes.

- Vasya Pupkin

## Protected paths

Changing any of these requires approval from an approved human reviewer (listed above).
Record it in the change review, item 7: each changed path, the reviewer's name, and the date.

- `AGENTS.md`, `constitution.md`, `CONTRIBUTING.md`
- `docs/standards.md`
- `specs/TEMPLATE.md`, `plans/TEMPLATE.md`, `tasks/TEMPLATE.md`
- `review/change-template.md`
- `skills/**`
- `scripts/validate.py`
- `.gitignore`
- In `specs/*.md`: setting `Status` to `Approved` or `Rejected`, or filling `Human approval`.
  Agents may set `Status` to `Draft` or `In Review`.
- In `docs/open-questions.md`: the `Answer` and `Resolved by` columns.
  Agents may add new questions under **Open**.

`python scripts/validate.py` cannot detect protected-path changes or per-spec scope;
the change review and a human reviewer check these.

## Secret-handling rules

- Never commit secrets: keys, tokens, passwords, private keys, connection strings.
- Store local secrets only in `.env` or `*.local` files; both are git-ignored.
- Never print, echo, log, or paste a secret into chat, docs, or skill runs.
- Use placeholders such as `<API_KEY>` in docs and examples.
- If a secret is exposed, stop, tell a human, and treat it as compromised.

## Conditions requiring human input

Stop and ask a human when any answer is Yes:

- Is a requirement missing, ambiguous, or contradictory?
- Does the work need a specification approved, or a status changed to `Approved`/`Rejected`?
- Does the change touch a protected path?
- Does the change add, remove, or upgrade a dependency?
- Does the change affect security, authentication, data, or secrets?
- Would passing validation require weakening a test or check?
- Is the work outside the approved specification's scope?
- Is there an entry in [docs/open-questions.md](docs/open-questions.md) that blocks the task?

When you stop:

1. Record the question under **Open** in [docs/open-questions.md](docs/open-questions.md), or in the spec's **Open Questions**.
2. Ask a human and make no further changes that depend on the answer.
3. Resume only after an approved reviewer records the answer, their name, and the date.
