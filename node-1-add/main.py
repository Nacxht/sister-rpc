import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv
from jsonrpcserver import Success, dispatch, method

from common.rpc_client import call_rpc

load_dotenv()

HOST = os.getenv("NODE_1_HOST", "0.0.0.0")
PORT = int(os.getenv("NODE_1_PORT", "5001"))


@method
def add(a, b):
    print(f"[ADD] {a} + {b}")

    result = a + b

    next_result = call_rpc(
        os.getenv("NODE_3_URL", "http://192.168.161.16:5003"),
        "multiply",
        [result, 2],
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

    print(f"Node 1 - ADD server running on port {PORT}")

    server.serve_forever()
