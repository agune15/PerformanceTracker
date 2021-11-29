"""
Module to track the performance of the CPU & RAM and log their status when a certain threshold is exceeded
"""

import time
import argparse
from classes.CPUTracker import CPUTracker
from classes.MemoryTracker import MemoryTracker
from classes.PerformanceLogger import PerformanceLogger

# Tracker config params
cpu_perc_threshold = 70
mem_MB_threshold = 3000
process_amount = 5

def main():
    parse_arguments()
    track_performance()

def track_performance():
    cpu_tracker = CPUTracker()
    mem_tracker = MemoryTracker()
    while(True):
        time.sleep(1)
        cpu_tracker.track_performance(perc_threshold=cpu_perc_threshold, process_amount=process_amount)
        mem_tracker.track_performance(MB_threshold=mem_MB_threshold, process_amount=process_amount)

#region Argument parsing

def parse_arguments():
    parser = create_parser_args()
    parse_argument_parser(parser)

def create_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ct", "--cputh", nargs='?', type=int, metavar="[0-100]%", default=None,
                        help=f"CPU usage percentage threshold. Default is {round(cpu_perc_threshold, 2)}")
    parser.add_argument("-mt", "--memth", nargs="?", type=int, metavar="MBs", default=None,
                        help=f"Memory usage MB threshold. Default is {round(mem_MB_threshold,2)} MB")
    parser.add_argument("-ld", "--logsdir", nargs="?", type=str, metavar="DIRECTORY", default=None,
                        help="Root directory for the logs to be stored. Ex: /home/userdir. Default is "
                             "PerformanceTracker.py's directory")
    parser.add_argument("-pa", "--pamount", nargs="?", type=int, metavar="processAmount", default=None,
                        help=f"Amount of processes to store in a log. Default is {round(process_amount)}")
    return parser

def parse_argument_parser(parser):
    global cpu_perc_threshold, mem_MB_threshold, process_amount

    args = vars(parser.parse_args())
    if args["cputh"] is not None:
        cpu_perc_threshold = args["cputh"]
    if args["memth"] is not None:
        mem_MB_threshold = args["memth"]
    if args["logsdir"] is not None:
        PerformanceLogger.set_logs_root_dir(args["logsdir"])
    if args["pamount"] is not None:
        process_amount = args["pamount"]

#endregion

if __name__ == "__main__":
    main()
