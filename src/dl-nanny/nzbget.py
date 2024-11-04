import requests
import json
import os

# Load NZBGet configuration from environment variables
NZBGET_URL = os.getenv("NZBGET_URL", "http://192.168.11.100:6789/jsonrpc")
NZBGET_USER = os.getenv("NZBGET_USER", "mntuser")
NZBGET_PASS = os.getenv("NZBGET_PASS", "gdgX001~")

# Set up authentication
auth = (NZBGET_USER, NZBGET_PASS)

# Example request to check NZBGet status
payload = {
    "method": "status",
    "params": [],
    "id": 1
}

# Send request to NZBGet's JSON-RPC API
response = requests.post(NZBGET_URL, data=json.dumps(payload), auth=auth)

# Parse response
if response.status_code == 200:
    status = response.json()
    print("NZBGet Status:", status)
else:
    print("Failed to connect to NZBGet:", response.status_code, response.text)
