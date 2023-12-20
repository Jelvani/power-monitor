import asyncio
from kasa import SmartPlug
import datetime
import os
import time
import argparse


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + str(counter) + extension
        counter += 1

    return path

async def main():
    parser = argparse.ArgumentParser(
                    prog='monitor.py',
                    description='Log power usage from TP-Link Kasa smartplugs')
    parser.add_argument('IP',help="IP address of a TP-Link Kasa smartplug.")  
    args = parser.parse_args()
    dev = SmartPlug(args.IP)  # We create the instance inside the main loop
    with open(uniquify("log.txt"), 'a+') as f:
        while True:
            await dev.update()  # Request an update
            watts = await dev.current_consumption()
            now = time.mktime(datetime.datetime.now().timetuple())
            print(watts)
            f.write("{} {}\n".format(now,watts))
            await asyncio.sleep(1)  # Sleep some time between updates
            

if __name__ == "__main__":
    asyncio.run(main())