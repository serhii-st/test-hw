"""Minimal HTTP server with a health endpoint (spec 0002)."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8000
HEALTH_BODY = json.dumps({"status": "OK"}).encode("utf-8")


class HealthHandler(BaseHTTPRequestHandler):
    """Serve GET /health. Other GET paths get 404; other methods get the default 501."""

    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(HEALTH_BODY)))
        self.end_headers()
        self.wfile.write(HEALTH_BODY)

    def log_message(self, format, *args):
        pass


def make_server(host=HOST, port=PORT):
    return HTTPServer((host, port), HealthHandler)


def main():
    with make_server() as server:
        print(f"Serving on http://{HOST}:{PORT}/health")
        server.serve_forever()


if __name__ == "__main__":
    main()
