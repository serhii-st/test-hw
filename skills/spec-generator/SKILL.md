---
name: spec-generator
description: Turn a change request into a Draft specification that follows specs/TEMPLATE.md.
---

# spec-generator

## Purpose and when to use it

Converts a plain-language request into a Draft spec. Use it at the start of any
feature or behavior change, before a plan or code exists.

## Required inputs

- Request text from a human.
- Next free spec number `NNNN` (check `specs/`).
- Any linked context the human supplied (issues, notes).

## Steps

1. Read [specs/TEMPLATE.md](../../specs/TEMPLATE.md), [constitution.md](../../constitution.md), and [docs/standards.md](../../docs/standards.md).
2. Restate the problem in one to three sentences using only facts from the request.
3. Write Scope and Out of Scope. Put anything the request does not mention in Out of Scope or Open Questions.
4. Write numbered requirements `R1..Rn`, each one testable and using "must".
5. Write at least one Given/When/Then acceptance criterion per requirement, tagged with its requirement ID.
6. Fill Security and Dependencies. Default to "None" only if the request clearly implies none.
7. Record every unknown under Open Questions. Do not invent answers.
8. Set `Status: Draft`. Leave Human approval blank.

## Stop conditions

Stop and ask a human, producing no spec, when:

- The request has no identifiable problem or user.
- The request conflicts with [constitution.md](../../constitution.md) or [AGENTS.md](../../AGENTS.md).
- You are asked to set Status to Approved or to fill Human approval.

## Output format

A complete markdown file for `specs/NNNN-short-name.md` using the template headings in order,
followed by a one-line summary: `Draft spec NNNN created with X requirements and Y open questions.`

## Quality checks (all must be Yes)

- Is Status exactly `Draft`?
- Does every requirement have at least one acceptance criterion?
- Is every acceptance criterion in Given/When/Then form?
- Is every fact traceable to the request or recorded as an open question?
- Is Human approval blank?
- Are all template headings present?

## Example

Input: "NNNN=0007. Users should be able to reset their password by email."

Output (abridged):

```markdown
# Spec 0007: Password reset by email
Status: Draft
## Requirements
- R1: The system must email a single-use reset link to a registered address.
## Acceptance Criteria
- AC1 (R1): Given a registered email, When the user requests a reset, Then one reset email is sent.
## Open Questions
- How long must a reset link stay valid?
## Human approval
- Approved by:
- Date:
```

`Draft spec 0007 created with 1 requirement and 1 open question.`
