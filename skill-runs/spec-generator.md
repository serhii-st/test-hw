# Skill run: spec-generator

- Skill: [skills/spec-generator/SKILL.md](../skills/spec-generator/SKILL.md)
- Date: 2026-09-30
- Runner: AI agent
- Decisions in force: [docs/open-questions.md](../docs/open-questions.md) Q1–Q6 (Python 3.10+, `unittest`, no CI, no new dependencies).
- Filed as: [specs/0001-title-to-url-slug.md](../specs/0001-title-to-url-slug.md) (Status: Draft), on human request so `test-plan-generator` can take its input from `specs/`.

## Input

```text
NNNN=0001.
Request: "Blog authors need readable, URL-safe addresses for their posts. Add a Python
function that turns a post title into a slug, for example 'Hello World' becomes
'hello-world'. Characters other than letters, digits, and spaces should be dropped."
Context: none beyond the request.
```

## Output

```markdown
# Spec 0001: Title to URL slug

Status: Draft

## Problem

Blog authors need readable, URL-safe addresses for their posts. There is no function
that turns a post title into such an address.

## Scope

- Provide one Python function that takes a title string and returns a slug string.

## Out of Scope

- Storing slugs or checking them for uniqueness.
- Web routing, HTTP handling, or any user interface.

## Requirements

- R1: The function must convert all letters in the title to lowercase.
- R2: The function must replace spaces with hyphens.
- R3: The function must drop every character that is not a letter, a digit, or a space.

## Acceptance Criteria

- AC1 (R1): Given the title `ABC`, When it is converted, Then the result is `abc`.
- AC2 (R2): Given the title `Hello World`, When it is converted, Then the result is `hello-world`.
- AC3 (R3): Given the title `Hello, World!`, When it is converted, Then the result is `hello-world`.

## Security and Dependencies

- Security impact: The title is untrusted input. The function only transforms a string; it performs no I/O and handles no secrets.
- New dependencies: None. The Python 3.10+ standard library is sufficient.

## Open Questions

- Should consecutive spaces become one hyphen or several (`a  b` → `a-b` or `a--b`)?
- Should leading and trailing spaces be trimmed before conversion?
- Do "letters" include non-ASCII letters such as `é` or `ß`, or only `a–z`?
- Existing hyphens are not letters, digits, or spaces, so R3 drops them (`well-known` → `wellknown`). Is that intended?
- What must the function return for an empty title, or a title with no letters or digits?
- Is there a maximum slug length?

## Human approval

- Approved by:
- Date:
```

Draft spec 0001 created with 3 requirements and 6 open questions.

## Quality checks

| Check | Answer |
|-------|--------|
| Is Status exactly `Draft`? | Yes |
| Does every requirement have at least one acceptance criterion? | Yes (R1: AC1; R2: AC2; R3: AC3) |
| Is every acceptance criterion in Given/When/Then form? | Yes |
| Is every fact traceable to the request or recorded as an open question? | Yes (R1–R3 and AC2 come from the request; whitespace, Unicode, hyphen, empty-input, and length behavior are open questions) |
| Is Human approval blank? | Yes |
| Are all template headings present? | Yes |
