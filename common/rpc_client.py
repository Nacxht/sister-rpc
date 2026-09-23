import json
from urllib.request import Request, urlopen

from jsonrpcclient import request


def call_rpc(server_url, method, params):
    rpc_request = request(
        method,
        params=params,
    )

    request_body = json.dumps(rpc_request).encode("utf-8")

    http_request = Request(
        server_url,
        data=request_body,
        headers={
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urlopen(http_request) as response:
        response_body = response.read().decode("utf-8")

    response_data = json.loads(response_body)

    if "error" in response_data:
        raise RuntimeError(response_data["error"])

    return response_data["result"]
