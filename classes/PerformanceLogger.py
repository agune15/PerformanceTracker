import subprocess

class PerformanceLogger:
    cpu_usage_top_processes = ""
    mem_usage_top_processes = ""

    @classmethod
    def store_cpu_top_processes(cls, process_amount):
        cls.cpu_usage_top_processes = subprocess.run(["top", "-b", "-o", "%CPU", "-n", "1"],
                                                     stdout=subprocess.PIPE).stdout.decode('ascii')
        cls.cpu_usage_top_processes = '\n'.join(cls.cpu_usage_top_processes.split('\n')[6:7+process_amount])

    @classmethod
    def store_mem_top_processes(cls, process_amount):
        cls.mem_usage_top_processes = subprocess.run("top -b -o %MEM | head -h " + str(7 + process_amount),
                                                     stdout=subprocess.PIPE).stdout
