from jsonrpcserver import Success, method

from common.rpc_client import call_rpc


@method
def multiply(a, b):
    print(f"[MULTIPLY] {a} * {b}")

    result = a * b

    next_result = call_rpc(
        "http://<IP-NODE-2>:5002",
        "subtract",
        [result, 3],
    )

    return Success(next_result)
