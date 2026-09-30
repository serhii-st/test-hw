# Change Review: Governance rule fixes (2026-09-30)

Type: `docs` / `chore`. No feature code. Completed from [change-template.md](change-template.md).

| # | Question | Answer | Evidence |
|---|----------|--------|----------|
| 1 | Is an approved specification linked? | Not applicable | Governance-only change; no `src/` change. |
| 2 | Is the change within scope? | Yes | Fixes the four findings of the rule-explicitness review only. |
| 3 | Are acceptance criteria covered by tests? | Not applicable | No spec. New validator checks exercised with negative cases (see 4). |
| 4 | Did validation pass? | Yes | `python scripts/validate.py` → `VALIDATION PASSED`, exit 0. Negative cases each produced the expected `FAIL`. |
| 5 | Are secrets absent? | Yes | Secret scan in `validate.py` passed. |
| 6 | Are dependencies justified? | Not applicable | No manifest changed. |
| 7 | Are protected paths unchanged or approved? | Yes | `AGENTS.md`, `CONTRIBUTING.md`, `review/change-template.md`, `skills/pr-reviewer/SKILL.md`, `scripts/validate.py` — approved by Vasya Pupkin, 2026-09-30 (confirmed by Serhii Stramnov). |
| 8 | Are relevant documents updated? | Yes | AGENTS.md, CONTRIBUTING.md, change template, pr-reviewer skill. |

## Changes

1. Spec `Status` protection narrowed to `Approved`/`Rejected` and `Human approval`; agents may set `Draft`/`In Review` (AGENTS.md, CONTRIBUTING.md).
2. Protected-path approval must name an approved reviewer and a date in item 7 (AGENTS.md, change template, pr-reviewer).
3. `Answer` and `Resolved by` in `docs/open-questions.md` are protected; `validate.py` enforces reviewer name and date.
4. Stop-and-ask now says what to do while waiting; `validate.py` rejects plans/tasks without a matching Approved spec; AGENTS.md states what the validator cannot check.

## Exceptions

- None.
