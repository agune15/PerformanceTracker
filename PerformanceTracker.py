import os.path
import time
from classes.CPUTracker import CPUTracker

def main():
    cpu_tracker = CPUTracker()
    while(True):
        time.sleep(1)
        cpu_tracker.track_performance(threshold=70, process_amount=5)

if __name__ == "__main__":
    main()
