import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Add parent directory to path to import common module
sys.path.append(str(Path(__file__).parent.parent))

from common.rpc_client import call_rpc

load_dotenv()

NODE_1_URL = os.getenv("NODE_1_URL", "http://192.168.161.137:5001")


if __name__ == "__main__":
    result = call_rpc(
        NODE_1_URL,
        "add",
        [10, 5],
    )

    print(f"\nFinal result: {result}")
