# AI-Ready Project Foundation

Governance, templates, validation, and reusable AI skills for a spec-driven project.
There is no feature code yet.

## Start here

- Agents: read [AGENTS.md](AGENTS.md) first.
- Humans: read [CONTRIBUTING.md](CONTRIBUTING.md) and [constitution.md](constitution.md).

## Workflow

request → specification → human approval → plan → tasks → implementation → validation → review

## Validate

Requires Python 3.10 or newer.

```bash
python scripts/validate.py
```

When `tests/` contains tests, also run:

```bash
python -m unittest discover -s tests -v
```

## Status

- Generic Python project. Tests use `unittest`.
- No CI and no license for now.
- Decisions: [docs/open-questions.md](docs/open-questions.md).
