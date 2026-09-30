# Skill run: test-plan-generator

- Skill: [skills/test-plan-generator/SKILL.md](../skills/test-plan-generator/SKILL.md)
- Date: 2026-09-30
- Runner: AI agent
- Decisions in force: [docs/open-questions.md](../docs/open-questions.md) Q1–Q6 (Python 3.10+, `unittest`, no CI).

## Input

```text
Spec: specs/0001-title-to-url-slug.md (Draft spec 0001 "Title to URL slug", Status: Draft).
Test runner: unittest (AGENTS.md).
```

## Output

Spec: [specs/0001-title-to-url-slug.md](../specs/0001-title-to-url-slug.md), Status: Draft

### Test cases

Target file for all tests: `tests/test_slug.py`, one `unittest.TestCase` class.
The module name `slug` is provisional; the plan for spec 0001 must confirm it.

| ID | Name | Criterion | Type | Preconditions | Steps | Expected |
|----|------|-----------|------|---------------|-------|----------|
| TC1 | test_uppercase_title_returns_lowercase | AC1 | unit | Slug function implemented per R1–R3 | Call the function with `ABC` | The result is `abc` |
| TC2 | test_title_with_space_returns_hyphenated | AC2 | unit | Slug function implemented per R1–R3 | Call the function with `Hello World` | The result is `hello-world` |
| TC3 | test_title_with_punctuation_returns_punctuation_dropped | AC3 | unit | Slug function implemented per R1–R3 | Call the function with `Hello, World!` | The result is `hello-world` |

No negative or edge tests were added: AC1–AC3 define no failure path or boundary.
The candidate edge cases depend on the unanswered questions below.

### Coverage

| Criterion | Test IDs | Covered |
|-----------|----------|---------|
| AC1 | TC1 | Yes |
| AC2 | TC2 | Yes |
| AC3 | TC3 | Yes |

### Open questions

- Edge tests for consecutive spaces, leading or trailing spaces, non-ASCII letters, existing hyphens, empty input, and maximum length wait on the matching spec 0001 open questions.
- Spec is Draft: re-check this plan after human approval.

## Quality checks

| Check | Answer |
|-------|--------|
| Does every acceptance criterion have at least one test? | Yes |
| Does every test trace to exactly one acceptance criterion? | Yes |
| Does every expected result match the criterion's Then clause? | Yes (copied verbatim) |
| Do all test names follow `test_<behavior>_<expected_result>`? | Yes |
| Are invented values absent (unknowns are open questions)? | Yes (module name marked provisional) |
