# Plan 0002: Health endpoint

- Spec: [specs/0002-health-endpoint.md](../specs/0002-health-endpoint.md)
- Spec status is Approved: Yes (Vasya Pupkin, 2026-09-30)

## Approach

One module, `src/health_server.py`, with a `BaseHTTPRequestHandler` subclass that defines only
`do_GET`. `GET /health` returns 200 with JSON `{"status": "OK"}`; any other GET path returns 404.
Because no other `do_<METHOD>` exists, `http.server` returns its default 501 for non-GET methods.
A `make_server()` function binds `localhost:8000` by default; tests pass port `0` to use a free port.
Running `python src/health_server.py` starts the server.

## Changes by file

| File | Change | Requirement |
|------|--------|-------------|
| `src/health_server.py` | `HOST`, `PORT`, `HealthHandler`, `make_server()`, `main()` | R1–R5 |
| `tests/test_health_server.py` | One test per acceptance criterion | AC1–AC5 |

## Dependencies

- None. Standard library only (`http.server`, `json`).

## Risks and mitigations

- Port 8000 already in use during tests → only the AC1 test binds 8000; other tests use port `0`.
- Handler logging request lines to stderr clutters test output → override `log_message` to stay silent.

## Validation

- Commands: `python scripts/validate.py` and `python -m unittest discover -s tests -v`
- Expected result: `VALIDATION PASSED` and `OK`, both with exit code `0`.
