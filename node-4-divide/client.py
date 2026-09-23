import os

from dotenv import load_dotenv
from jsonrpcserver import Success, method

load_dotenv()


@method
def divide(a, b):
    print(f"[DIVIDE] {a} / {b}")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return Success(a / b)
