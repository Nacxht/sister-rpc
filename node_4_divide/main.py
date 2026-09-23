import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from dotenv import load_dotenv
from jsonrpcserver import Success, dispatch, method

# Add parent directory to path to import common module
sys.path.append(str(Path(__file__).parent.parent))

load_dotenv()

HOST = os.getenv("NODE_4_HOST", "0.0.0.0")
PORT = int(os.getenv("NODE_4_PORT", "5004"))


@method
def divide(a, b):
    print(f"[DIVIDE] {a} / {b}")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return Success(a / b)


class RPCHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(content_length).decode("utf-8")

        response = dispatch(request_body)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(response.encode("utf-8"))

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RPCHandler)

    print(f"Node 4 - DIVIDE server running on port {PORT}")

    server.serve_forever()
