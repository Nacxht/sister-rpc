from jsonrpcserver import Success, method


@method
def divide(a, b):
    print(f"[DIVIDE] {a} / {b}")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return Success(a / b)
