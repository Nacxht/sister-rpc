import urllib.request

from jsonrpcclient import request

SERVER_URL = "http://127.0.0.1:5002"


req = request("add", 10, 5)

with urllib.request.urlopen(
    SERVER_URL,
    data=req.encode(),
    headers={"Content-Type": "application/json"},
) as response:
    result = response.read().decode()

print("Response:", result)
