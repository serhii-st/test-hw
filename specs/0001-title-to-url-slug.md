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
