"""
Class to track the performance of the CPU
"""

import os.path

CPU_STATS_PATH = "/proc/stat"

class CPUTracker:
    def __init__(self):
        self.last_working_time, self.last_idle_time = self.get_cpu_times()

    def get_cpu_times(self):
        with open(CPU_STATS_PATH) as statfile:
            cpustats = statfile.readline().split()
            working_time = int(cpustats[1]) + int(cpustats[2]) + int(cpustats[3])
            idle_time = int(cpustats[4] + cpustats[5])
            return working_time, idle_time

    def get_usage_percentage(self):
        curr_working_time, curr_idle_time = self.get_cpu_times()
        working_time = curr_working_time - self.last_working_time
        idle_time = curr_idle_time - self.last_idle_time
        total_time = working_time + idle_time
        usage_perc = (working_time / total_time) * 100
        return usage_perc
