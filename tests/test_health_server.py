"""Tests for spec 0002: Health endpoint."""
import http.client
import json
import sys
import threading
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import health_server  # noqa: E402


class RunningServer:
    """Start a server in a background thread and stop it on exit."""

    def __init__(self, **kwargs):
        self.server = health_server.make_server(**kwargs)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self):
        self.thread.start()
        return self.server

    def __exit__(self, *exc):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()


def request(server, method, path):
    host, port = server.server_address[:2]
    conn = http.client.HTTPConnection(host, port, timeout=5)
    try:
        conn.request(method, path)
        resp = conn.getresponse()
        return resp.status, resp.getheader("Content-Type"), resp.read()
    finally:
        conn.close()


class HealthServerTest(unittest.TestCase):
    def test_default_server_on_localhost_8000_accepts_connection(self):  # AC1
        self.assertEqual(health_server.HOST, "localhost")
        self.assertEqual(health_server.PORT, 8000)
        with RunningServer() as server:
            conn = http.client.HTTPConnection("localhost", 8000, timeout=5)
            try:
                conn.connect()
            finally:
                conn.close()
            self.assertEqual(server.server_address[1], 8000)

    def test_get_health_returns_200(self):  # AC2
        with RunningServer(port=0) as server:
            status, _, _ = request(server, "GET", "/health")
        self.assertEqual(status, 200)

    def test_get_health_returns_json_status_ok(self):  # AC3
        with RunningServer(port=0) as server:
            _, content_type, body = request(server, "GET", "/health")
        self.assertEqual(content_type, "application/json")
        self.assertEqual(json.loads(body), {"status": "OK"})

    def test_get_unknown_path_returns_404(self):  # AC4
        with RunningServer(port=0) as server:
            status, _, _ = request(server, "GET", "/unknown")
        self.assertEqual(status, 404)

    def test_post_health_returns_501(self):  # AC5
        with RunningServer(port=0) as server:
            status, _, _ = request(server, "POST", "/health")
        self.assertEqual(status, 501)


if __name__ == "__main__":
    unittest.main()
