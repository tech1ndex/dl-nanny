from deluge_client import DelugeRPCClient
import os

# Connect to the remote Deluge daemon
HOST = os.environ.get('DELUGE_HOST')
PORT = os.environ.get('DELUGE_PORT')
USERNAME = os.environ.get('DELUGE_USERNAME')
PASSWORD = os.environ.get('DELUGE_PASSWORD')

client = DelugeRPCClient(HOST, PORT, USERNAME, PASSWORD)
client.connect()