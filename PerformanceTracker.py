"""
Module to track the performance of the CPU & RAM and log their status when a threshold is exceeded
"""

import time
from classes.CPUTracker import CPUTracker
from classes.MemoryTracker import MemoryTracker

def main():
    #TODO: Add into separate function
    cpu_tracker = CPUTracker()
    mem_tracker = MemoryTracker()
    while(True):
        time.sleep(1)
        cpu_tracker.track_performance(perc_threshold=70, process_amount=5)
        mem_tracker.track_performance(MB_threshold=3500, process_amount=5)

if __name__ == "__main__":
    main()
