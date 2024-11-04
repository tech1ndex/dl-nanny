import requests
import json
import os
from dotenv import load_dotenv


# Load NZBGet configuration from environment variables
load_dotenv()
NZBGET_URL = os.getenv("NZBGET_URL")
NZBGET_USER = os.getenv("NZBGET_USER")
NZBGET_PASS = os.getenv("NZBGET_PASS")

# Set up authentication
auth = (NZBGET_USER, NZBGET_PASS)

# Define the JSON-RPC payload for the `listgroups` method
payload = {
    "method": "listgroups",
    "params": [],
    "id": 1
}

# Send request to NZBGet's JSON-RPC API
response = requests.post(NZBGET_URL, data=json.dumps(payload), auth=auth)
# Check if the request was successful
if response.status_code == 200:
    active_nzbs = response.json().get("result", [])

    # Print details of each active NZB
    for nzb in active_nzbs:
        print(f"NZB Name: {nzb['NZBName']}")
        print(f"File Size: {nzb['FileSizeMB']} MB")
        print(f"Downloaded: {nzb['DownloadedSizeMB']} MB")
        print(f"Remaining: {nzb['RemainingSizeMB']} MB")
        print(f"Status: {nzb['Status']}")
        print("-" * 40)
else:
    print("Failed to connect to NZBGet:", response.status_code, response.text)