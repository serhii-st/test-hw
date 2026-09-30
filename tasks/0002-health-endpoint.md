# Tasks 0002: Health endpoint

- Spec: [specs/0002-health-endpoint.md](../specs/0002-health-endpoint.md)
- Plan: [plans/0002-health-endpoint.md](../plans/0002-health-endpoint.md)

Each task is small, traces to a requirement, and is done only when its check passes.

| ID | Task | Traces to | Done check (Yes/No) | Done |
|----|------|-----------|---------------------|------|
| T1 | Write failing `unittest` tests for AC1–AC5 | AC1–AC5 | Do the tests fail because `health_server` does not exist? | [x] |
| T2 | Implement server bound to `localhost:8000` | R1 | Does the AC1 test pass? | [x] |
| T3 | Implement `GET /health` → 200 | R2 | Does the AC2 test pass? | [x] |
| T4 | Return JSON `{"status": "OK"}` as `application/json` | R3 | Does the AC3 test pass? | [x] |
| T5 | Return 404 for other GET paths | R4 | Does the AC4 test pass? | [x] |
| T6 | Leave non-GET methods to the `http.server` default 501 | R5 | Does the AC5 test pass? | [x] |
| T7 | Run validation | All | Did every validation command in `AGENTS.md` pass? | [x] |
| T8 | Complete review checklist | All | Is every item answered with evidence? | [x] |
