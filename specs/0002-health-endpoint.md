# Spec 0002: Health endpoint

Status: Approved

## Problem

Operators and monitoring tools need a simple way to check that the service is running.
The project has no HTTP endpoint that reports service health.

## Scope

- Provide a minimal HTTP server using the standard library `http.server`, listening on `localhost:8000`.
- Provide one endpoint, `GET /health`, returning HTTP 200 with JSON `{"status": "OK"}`.

## Out of Scope

- Checking downstream dependencies (databases, external services).
- Authentication, metrics, or readiness/liveness distinctions.
- Any other endpoint, HTTP method, or third-party web framework.
- Configurable host or port.

## Requirements

- R1: The server must listen on host `localhost`, port `8000`, using the standard library `http.server`.
- R2: A `GET /health` request must receive HTTP status code 200.
- R3: The `GET /health` response body must be the JSON object `{"status": "OK"}` with `Content-Type: application/json`.
- R4: A `GET` request to any path other than `/health` must receive HTTP status code 404.
- R5: A non-GET request to `/health` must receive the `http.server` default response, HTTP status code 501.

## Acceptance Criteria

- AC1 (R1): Given the server is started, When a client connects to `localhost:8000`, Then the connection is accepted.
- AC2 (R2): Given the server is running, When a client sends `GET /health`, Then the response status code is 200.
- AC3 (R3): Given the server is running, When a client sends `GET /health`, Then the `Content-Type` header is `application/json` and the body parses as JSON equal to `{"status": "OK"}`.
- AC4 (R4): Given the server is running, When a client sends `GET /unknown`, Then the response status code is 404.
- AC5 (R5): Given the server is running, When a client sends `POST /health`, Then the response status code is 501.

## Security and Dependencies

- Security impact: Opens a network listener bound to `localhost` only. The response reveals no internal details, versions, or secrets. Request path and headers are untrusted input.
- New dependencies: None. The Python 3.10+ standard library (`http.server`, `json`) is sufficient.

## Open Questions

- Answered by Serhii Stramnov, 2026-09-30: path `/health`; body JSON `{"status": "OK"}`; server `http.server`; bind `localhost:8000`; method GET only; unknown paths return 404; non-GET requests to `/health` return the `http.server` default 501.

## Human approval

- Approved by: Vasya Pupkin
- Date: 2026-09-30
