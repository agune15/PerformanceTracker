"""
TODO
"""

from .PerformanceLogger import PerformanceLogger

MEM_INFO_PATH = "/proc/meminfo"

class MemoryTracker:
    def __init__(self):
        self.total_memory_KiB = self.get_total_memory_KiB()

    def track_performance(self, MB_threshold, process_amount):
        total_mem_MB = self.total_memory_KiB * 1.024 / 1000
        if not 0 <= MB_threshold <= total_mem_MB:
            raise AssertionError(f"Memory usage MB threshold be between 0 and {total_mem_MB}")

        PerformanceLogger.store_mem_top_processes(process_amount)
        used_memory_KiB = self.get_used_memory_KiB()
        used_mem_MB = used_memory_KiB * 1.024 / 1000

        if used_mem_MB > MB_threshold:
            print(f"Memory usage exceeds threshold: {round(used_mem_MB,2)} MB > {round(MB_threshold,2)} MB. "
                  f"Total: {round(total_mem_MB,2)} MB")
            print(PerformanceLogger.mem_usage_top_processes + "\n")
            PerformanceLogger.store_mem_log()

    def get_total_memory_KiB(self):
        with open(MEM_INFO_PATH) as memfile:
            meminfo = memfile.readline().split()
            total_memory = int(meminfo[1])
            return total_memory

    def get_used_memory_KiB(self):
        with open(MEM_INFO_PATH) as memfile:
            next(memfile)
            next(memfile)
            meminfo = memfile.readline().split()
            used_memory = self.total_memory_KiB - int(meminfo[1])
            return used_memory