import json
from urllib.request import Request, urlopen

from jsonrpcclient import request

SERVER_URL = "http://127.0.0.1:5002"


rpc_request = request(
    "add",
    params=[10, 5],
)

request_body = json.dumps(rpc_request).encode("utf-8")

http_request = Request(
    SERVER_URL,
    data=request_body,
    headers={
        "Content-Type": "application/json",
    },
    method="POST",
)


with urlopen(http_request) as response:
    result = response.read().decode("utf-8")


print("Response:", result)
