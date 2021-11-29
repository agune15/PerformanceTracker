"""
Class to track the performance of the CPU
"""

from .PerformanceLogger import PerformanceLogger

CPU_STATS_PATH = "/proc/stat"

class CPUTracker:
    def __init__(self):
        self.last_working_time, self.last_idle_time = self.__get_cpu_times()

    def track_performance(self, perc_threshold, process_amount):
        if not (0 <= perc_threshold <= 100):
            raise AssertionError("CPU usage percentage threshold has to be between 0 and 100")

        PerformanceLogger.store_cpu_top_processes(process_amount)
        cpu_usage = self.__get_usage_percentage()

        if cpu_usage > perc_threshold:
            log = PerformanceLogger.store_cpu_log(cpu_usage, perc_threshold)
            print(log)

    def __get_usage_percentage(self):
        curr_working_time, curr_idle_time = self.__get_cpu_times()
        working_time = curr_working_time - self.last_working_time
        idle_time = curr_idle_time - self.last_idle_time
        total_time = working_time + idle_time

        self.last_working_time = curr_working_time
        self.last_idle_time = curr_idle_time

        usage_perc = (working_time / total_time) * 100
        return usage_perc

    def __get_cpu_times(self):
        with open(CPU_STATS_PATH) as statfile:
            cpustats = statfile.readline().split()
            working_time = int(cpustats[1]) + int(cpustats[2]) + int(cpustats[3])
            idle_time = int(cpustats[4]) + int(cpustats[5])
            return working_time, idle_time
