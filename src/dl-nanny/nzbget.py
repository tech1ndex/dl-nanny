
import pynzbget
import os

nzbget_url = os.getenv("NZBGET_URL", "http://192.168.11.100:6789")
nzbget_user = os.getenv("NZBGET_USER", "mntuser")
nzbget_pass = os.getenv("NZBGET_PASS", "gdgX001~")


# Replace these with your actual host and port if they're different
nzbget = NZBGet(nzbget_url, username=nzbget_user, password=nzbget_pass)

# Check if NZBGet is running
if nzbget.status():
    print("NZBGet is running!")
else:
    print("NZBGet is not running.")

# Get the current download queue
queue = nzbget.listgroups()
print("Current queue:", queue)

# Add an NZB file to the queue
nzb_file_path = "/path/to/your/file.nzb"
with open(nzb_file_path, "rb") as nzb_file:
    nzb_content = nzb_file.read()
nzbget.append(nzb_content, "example_name")

# Pause or resume downloads
nzbget.pause()
# ... later
nzbget.resume()
