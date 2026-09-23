import os

from dotenv import load_dotenv
from jsonrpcserver import Success, method

from common.rpc_client import call_rpc

load_dotenv()


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
