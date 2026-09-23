from common.rpc_client import call_rpc

NODE_1_URL = "http://192.168.161.137:5001"


if __name__ == "__main__":
    result = call_rpc(
        NODE_1_URL,
        "add",
        [10, 5],
    )

    print(f"\nFinal result: {result}")
