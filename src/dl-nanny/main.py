import schedule
import time
import deluge

def main():
    get_torrents()

schedule.every(10).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
