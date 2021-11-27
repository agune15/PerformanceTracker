import os.path
import time
from classes import CPUTracker

def main():
    cpu_tracker = CPUTracker.CPUTracker()
    while(True):
        print("CPU usage: {perc}%".format(perc=cpu_tracker.get_usage_percentage()))
        time.sleep(1)

if __name__ == "__main__":
    main()

