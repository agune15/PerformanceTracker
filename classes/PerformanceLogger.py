"""
Class to log the performance of the CPU & RAM
"""

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

    #region CPU logging

    @classmethod
    def store_cpu_top_processes(cls, process_amount):
        cls.__assert_process_amount(process_amount)

        cls.cpu_usage_top_processes = subprocess.run(["top", "-b", "-o", "%CPU", "-n", "1"],
                                                     stdout=subprocess.PIPE).stdout.decode('ascii')
        cls.cpu_usage_top_processes = '\n'.join(cls.cpu_usage_top_processes.split('\n')[6:7+process_amount])

    @classmethod
    def store_cpu_log(cls, cpu_usage, perc_threshold):
        if not cls.any_logs_created:
            cls.__create_logs_dir()

        log = cls.__get_log_date() + " - "
        log += f"CPU usage exceeds threshold: {round(cpu_usage,2)}% > {round(perc_threshold,2)}%\n"
        log += cls.cpu_usage_top_processes + "\n"

        with open(cls.cpu_logs_file, "a+") as f:
            f.write(log + "\n")
        return log

    #endregion

    #region Memory logging

    @classmethod
    def store_mem_top_processes(cls, process_amount):
        cls.__assert_process_amount(process_amount)

        cls.mem_usage_top_processes = subprocess.run(["top", "-b", "-o", "%MEM", "-n", "1"],
                                                     stdout=subprocess.PIPE).stdout.decode('ascii')
        cls.mem_usage_top_processes = '\n'.join(cls.mem_usage_top_processes.split('\n')[6:7+process_amount])

    @classmethod
    def store_mem_log(cls, used_mem_MB, MB_threshold, total_mem_MB):
        if not cls.any_logs_created:
            cls.__create_logs_dir()

        log = cls.__get_log_date() + " - "
        log += f"Memory usage exceeds threshold: {round(used_mem_MB,2)} MB > {round(MB_threshold,2)} MB. " \
              f"Total: {round(total_mem_MB,2)} MB\n"
        log += cls.mem_usage_top_processes + "\n"

        with open(cls.mem_logs_file, "a+") as f:
            f.write(log + "\n")
        return log

    #endregion

    @classmethod
    def __get_log_date(cls):
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    @classmethod
    def __assert_process_amount(cls, process_amount):
        if process_amount <= 0:
            raise AssertionError("Process amount has to be greater than 1")

    @classmethod
    def __create_logs_dir(cls):
        if not cls.logs_path:
            cls.__set_logs_default_root_dir()
        logs_folder_name = datetime.now().strftime("%Y%m%d_%H%M")
        cls.logs_path = path.join(cls.logs_path, logs_folder_name)

        if not path.exists(cls.logs_path):
            makedirs(cls.logs_path)

        cls.cpu_logs_file = cls.logs_path + "/CPU"
        cls.mem_logs_file = cls.logs_path + "/MEM"
        cls.any_logs_created = True

    @classmethod
    def set_logs_root_dir(cls, logs_dir):
        if not path.exists(logs_dir):
            raise AssertionError(f"Directory {logs_dir} does not exist")

        cls.logs_path = logs_dir

    @classmethod
    def __set_logs_default_root_dir(cls):
        logs_path = path.abspath(sys.modules["__main__"].__file__)
        logs_path = logs_path.replace("PerformanceTracker.py", '')
        cls.set_logs_root_dir(logs_path)
