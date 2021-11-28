import os.path
import subprocess
import sys
from os import path, makedirs
from datetime import datetime

class PerformanceLogger:
    cpu_usage_top_processes = ""
    mem_usage_top_processes = ""
    any_logs_created = False
    logs_path = ""
    cpu_logs_file = ""
    mem_logs_file = ""

    @classmethod
    def store_cpu_top_processes(cls, process_amount):
        cls.cpu_usage_top_processes = subprocess.run(["top", "-b", "-o", "%CPU", "-n", "1"],
                                                     stdout=subprocess.PIPE).stdout.decode('ascii')
        cls.cpu_usage_top_processes = '\n'.join(cls.cpu_usage_top_processes.split('\n')[6:7+process_amount])

    @classmethod
    def store_mem_top_processes(cls, process_amount):
        cls.mem_usage_top_processes = subprocess.run(["top", "-b", "-o", "%MEM", "-n", "1"],
                                                     stdout=subprocess.PIPE).stdout.decode('ascii')
        cls.mem_usage_top_processes = '\n'.join(cls.cpu_usage_top_processes.split('\n')[6:7+process_amount])

    @classmethod
    def store_cpu_log(cls):
        if not cls.any_logs_created:
            cls.create_logs_dir()

        with open(cls.cpu_logs_file, "a+") as f:
            # TODO: Write CPU usage vs threshold
            f.write("usage of the CPU\n")
            f.write(cls.cpu_usage_top_processes + "\n\n")

    @classmethod
    def store_mem_log(cls):
        if not cls.any_logs_created:
            cls.create_logs_dir()

        with open(cls.mem_logs_file, "a+") as f:
            # TODO: Write MEM usage vs threshold
            f.write("usage of the MEM\n")
            f.write(cls.mem_usage_top_processes + "\n\n")

    @classmethod
    def create_logs_dir(cls):
        cls.logs_path = path.abspath(sys.modules["__main__"].__file__)
        cls.logs_path = cls.logs_path.replace("PerformanceTracker.py", '')
        logs_folder_name = datetime.now().strftime("%Y%m%d_%H%M")
        cls.logs_path = path.join(cls.logs_path, logs_folder_name)
        makedirs(cls.logs_path)
        cls.cpu_logs_file = cls.logs_path + "/CPU"
        cls.mem_logs_file = cls.logs_path + "/MEM"
        cls.any_logs_created = True
