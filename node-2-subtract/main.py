from http.server import BaseHTTPRequestHandler, HTTPServer

from jsonrpcserver import Success, dispatch, method

HOST = "0.0.0.0"
PORT = 5002


@method
def subtract(a, b):
    print(f"[SUBTRACT] {a} - {b}")
    return Success(a - b)


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

    print(f"Node 2 - SUBTRACT server running on port {PORT}")

    server.serve_forever()
