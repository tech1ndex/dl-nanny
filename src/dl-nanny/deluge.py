from deluge_client import DelugeRPCClient

# Connect to the Deluge daemon
client = DelugeRPCClient('127.0.0.1', 58846, 'username', 'password')
client.connect()

# Get the list of torrents
torrents = client.call('core.get_torrents_status', {}, ['name', 'progress'])

# Print out the name and progress of each torrent
for torrent_id, torrent_info in torrents.items():
    print(f"Torrent: {torrent_info[b'name'].decode()}")
    print(f"Progress: {torrent_info[b'progress']}%")

# Add a new torrent
magnet_link = "magnet:?xt=urn:btih:..."
client.call('core.add_torrent_magnet', magnet_link, {})

# Disconnect when done
client.disconnect()