from deluge_client import DelugeRPCClient
import os

# Connect to the remote Deluge daemon
HOST = "192.168.11.100"
PORT = 58846
USERNAME = os.environ.get('DELUGE_USERNAME')
PASSWORD = os.environ.get('DELUGE_PASSWORD')

client = DelugeRPCClient(HOST, PORT, USERNAME, PASSWORD)
client.connect()