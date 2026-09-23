import os

from dotenv import load_dotenv

from common.rpc_client import call_rpc

load_dotenv()

NODE_4_URL = os.getenv("NODE_4_URL", "http://192.168.161.238:5004")


if __name__ == "__main__":
    result = call_rpc(
        NODE_4_URL,
        "divide",
        [27, 9],
    )

    print("Node 4 response:", result)
