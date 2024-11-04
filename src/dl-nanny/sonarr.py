import os
import requests
from dotenv import load_dotenv

load_dotenv()
SONARR_URL = os.getenv("SONARR_URL")
SONARR_API_KEY = os.getenv("SONARR_API_KEY")

# Define headers for the API request
headers = {
    "X-Api-Key": SONARR_API_KEY
}

# Define the endpoint to get the activity queue
activity_url = f"{SONARR_URL}/api/v3/queue"

# Send a GET request to the queue endpoint
response = requests.get(activity_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    activity_queue = response.json()
    print(activity_queue)
    # Print details of each item in the queue
    if activity_queue:
        print("Current Sonarr Activity:")
        for item in activity_queue:
            print(item)
    else:
        print("No active downloads in the queue.")
else:
    print("Failed to retrieve activity queue:", response.status_code, response.text)