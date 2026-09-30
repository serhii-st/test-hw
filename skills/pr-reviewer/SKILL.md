---
name: pr-reviewer
description: Review a change against review/change-template.md and give a merge recommendation.
---

# pr-reviewer

## Purpose and when to use it

Checks a pull request or diff against the repository checklist in
[review/change-template.md](../../review/change-template.md). Use it before a human merges any change.

## Required inputs

- The diff or list of changed files.
- The linked spec (or a statement that none applies).
- Validation command output from the author, or permission to run it.

## Steps

1. Read [review/change-template.md](../../review/change-template.md) and [AGENTS.md](../../AGENTS.md) (protected paths, secret rules).
2. Run every applicable command in [AGENTS.md § Validation commands](../../AGENTS.md#validation-commands) if possible and capture the last lines of output.
3. Answer the eight checklist items, in the same order and wording as the template:
   1. Is an approved specification linked?
   2. Is the change within scope?
   3. Are acceptance criteria covered by tests?
   4. Did validation pass?
   5. Are secrets absent?
   6. Are dependencies justified?
   7. Are protected paths unchanged or approved?
   8. Are relevant documents updated?
4. For each item give exactly one of Yes, No, Not applicable, plus evidence (link, command output, or file reference).
5. List every No with the file and the fix needed.
6. Recommend `Approve for human merge` only if no item is No; otherwise `Changes requested`.

## Stop conditions

Stop and ask a human when:

- The diff or changed-file list is not available.
- A protected path changed and item 7 evidence does not name a reviewer listed in AGENTS.md and a date.
- A possible secret is found (report its file and line, never its value).

## Output format

The completed checklist table from the template, then `Findings:` (bulleted, or `None`),
then `Recommendation: Approve for human merge` or `Recommendation: Changes requested`.

## Quality checks (all must be Yes)

- Are all eight items answered in template order?
- Is every answer exactly Yes, No, or Not applicable?
- Does every answer have evidence?
- Is every No listed under Findings?
- Is no secret value reproduced?
- Does the recommendation follow the rule in step 6?

## Example

Input: "Diff adds `src/reset.py` and `tests/test_reset.py`; links specs/0007 (Approved); validation passed."

Output (abridged):

```markdown
| 1 | Is an approved specification linked? | Yes | specs/0007-password-reset.md, Status: Approved |
| 6 | Are dependencies justified? | Not applicable | No manifest changed |
Findings: None
Recommendation: Approve for human merge
```
