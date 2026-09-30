---
name: test-plan-generator
description: Map a specification's acceptance criteria to concrete, named test cases.
---

# test-plan-generator

## Purpose and when to use it

Produces a test plan that covers every acceptance criterion of a spec. Use it after
a spec is written (for review) and again when it is Approved (before implementation).

## Required inputs

- Path or content of one spec in `specs/`.
- The test runner from [AGENTS.md](../../AGENTS.md) (currently `unittest`).

## Steps

1. Read the spec and [docs/standards.md § Testing](../../docs/standards.md#testing).
2. List every acceptance criterion with its ID.
3. For each criterion write at least one positive test; add a negative or edge test when the criterion has a failure path or a boundary.
4. Name each test `test_<behavior>_<expected_result>` and give its target file `tests/test_<module>.py`.
5. For each test give type (unit, integration, manual), preconditions, steps, and expected result copied from the Then clause.
6. Build a coverage table: criterion → test IDs. Flag any criterion with no test.
7. Record unknowns (thresholds, data, environments) as open questions. Do not invent values.

## Stop conditions

Stop and ask a human when:

- The spec has no acceptance criteria.
- An acceptance criterion is not in Given/When/Then form.
- The Then clause is not observable (cannot be checked by a test).

## Output format

1. `Spec:` line with path and Status.
2. Test case table: ID, Name, Criterion, Type, Preconditions, Steps, Expected.
3. Coverage table: Criterion, Test IDs, Covered (Yes/No).
4. Open questions (or `None`).

## Quality checks (all must be Yes)

- Does every acceptance criterion have at least one test?
- Does every test trace to exactly one acceptance criterion?
- Does every expected result match the criterion's Then clause?
- Do all test names follow `test_<behavior>_<expected_result>`?
- Are invented values absent (unknowns are open questions)?

## Example

Input: "AC1 (R1): Given a registered email, When the user requests a reset, Then one reset email is sent."

Output (abridged):

```markdown
| ID | Name | Criterion | Type | Expected |
|----|------|-----------|------|----------|
| TC1 | test_reset_request_registered_email_sends_one_email | AC1 | integration | One reset email is sent |
| AC1 | TC1 | Yes |
Open questions: None
```
