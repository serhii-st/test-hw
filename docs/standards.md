# Standards

Each rule is answerable Yes or No. Each section has one good and one bad example.

## Naming

- Are non-Python files and folders lowercase kebab-case (except `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `TEMPLATE.md`, `SKILL.md`)?
- Are Python modules, packages, functions, and variables `snake_case`, classes `PascalCase`, and constants `UPPER_SNAKE_CASE` (PEP 8)?
- Are specs, plans, and tasks named `NNNN-short-name.md` with a shared number?
- Are branches named `<type>/NNNN-short-name` where type is `feat`, `fix`, `docs`, or `chore`?

Good: `specs/0003-user-login.md`, `src/user_login.py`, branch `feat/0003-user-login`
Bad: `specs/Login Spec FINAL.md`, `src/User-Login.py`, branch `my-changes`

## Change submission

- Does the pull request link exactly one approved spec (or state `Not applicable` for docs/chore)?
- Does the pull request description contain the completed [review checklist](../review/change-template.md)?
- Do commit messages use `<type>: <imperative summary>` under 72 characters?

Good: `feat: add login form validation (spec 0003)`
Bad: `stuff`, or one pull request covering specs 0003 and 0004

## Documentation

- Is every new governance file linked from [AGENTS.md](../AGENTS.md)?
- Is each file focused on one topic and under about 150 lines?
- Do all relative links resolve (checked by `python scripts/validate.py`)?

Good: a new `docs/logging.md` linked from AGENTS.md, 40 lines, one topic.
Bad: a 600-line `docs/notes.md` mixing setup, decisions, and todo items, linked nowhere.

## Dependencies

- Is the Python standard library insufficient for the requirement?
- Is each new dependency required by an approved spec requirement?
- Is its version pinned and its license recorded in the plan?
- Did an approved reviewer (AGENTS.md) approve the addition?

Good: plan states "Add `requests==2.32.3` (Apache-2.0) for R2 HTTP retries; approved by Vasya Pupkin 2026-10-01."
Bad: `pip install requests` unpinned, to make one GET call `urllib.request` already handles, not in any spec.

## Security

- Are secrets absent from the repository and replaced with placeholders in docs?
- Is all external input validated before use?
- Are security checks and tests unchanged or strengthened?

Good: `API_KEY=<API_KEY>` in `.env.example`; real value in git-ignored `.env`.
Bad: `API_KEY=sk_live_...` committed in `config.py`, or a failing auth test marked skip.

## Testing

- Are tests written with `unittest` in `tests/test_<module>.py`, as `unittest.TestCase` methods?
- Does every Given/When/Then acceptance criterion map to at least one test?
- Do test method names follow `test_<behavior>_<expected_result>`?
- Does `python -m unittest discover -s tests -v` pass locally before submission?

Good: `tests/test_user_login.py` with `test_login_wrong_password_returns_401` covering AC2.
Bad: `tests/checks.py` with `test1` asserting `True`, or `@unittest.skip` added to a failing test to make it pass.
