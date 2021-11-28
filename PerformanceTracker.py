import os.path
import time
from classes import CPUTracker

def main():
    cpu_tracker = CPUTracker.CPUTracker()
    while(True):
        time.sleep(1)
        cpu_tracker.track_performance(70)

if __name__ == "__main__":
    main()
