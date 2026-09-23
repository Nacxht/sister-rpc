from jsonrpcserver import method, serve


@method
def add(a, b):
    print(f"[ADD] {a} + {b}")
    return a + b


if __name__ == "__main__":
    print("RPC Server running on port 5002...")
    serve(port=5002)
