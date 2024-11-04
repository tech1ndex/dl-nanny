from deluge_client import DelugeRPCClient
import os

# Connect to the remote Deluge daemon
HOST = "192.168.11.100"
PORT = 58846
USERNAME = os.environ.get('DELUGE_USERNAME')
PASSWORD = os.environ.get('DELUGE_PASSWORD')

client = DelugeRPCClient(HOST, PORT, USERNAME, PASSWORD)
client.connect()


def get_torrents():
    # Get list of torrents
    torrents = client.call('core.get_torrents_status', {}, ['name', 'progress'])
    for torrent_id, torrent_info in torrents.items():
        print(f"Torrent: {torrent_info[b'name'].decode()}")
        print(f"Progress: {torrent_info[b'progress']}%")

    # Add a new torrent
    magnet_link = "magnet:?xt=urn:btih:..."
    client.call('core.add_torrent_magnet', magnet_link, {})

    # Disconnect when done
    client.disconnect()