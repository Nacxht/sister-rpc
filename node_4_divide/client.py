import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from jsonrpcserver import Success, method

# Add parent directory to path to import common module
sys.path.append(str(Path(__file__).parent.parent))

load_dotenv()


@method
def divide(a, b):
    print(f"[DIVIDE] {a} / {b}")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return Success(a / b)
