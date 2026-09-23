import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from dotenv import load_dotenv
from jsonrpcserver import Success, dispatch, method

# Add parent directory to path to import common module
sys.path.append(str(Path(__file__).parent.parent))

from common.rpc_client import call_rpc

load_dotenv()

HOST = os.getenv("NODE_3_HOST", "0.0.0.0")
PORT = int(os.getenv("NODE_3_PORT", "5003"))


@method
def multiply(a, b):
    print(f"[MULTIPLY] {a} * {b}")

    result = a * b

    next_result = call_rpc(
        os.getenv("NODE_2_URL", "http://192.168.161.238:5002"),
        "subtract",
        [result, 3],
    )

    return Success(next_result)


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

    print(f"Node 3 - MULTIPLY server running on port {PORT}")

    server.serve_forever()
