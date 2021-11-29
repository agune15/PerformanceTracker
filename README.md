# PerformanceTracker
CPU &amp; RAM performance tracker for Linux

## Functionality
- Monitor CPU & RAM utilization in runtime for Linux OS
- When CPU/RAM usage is above the defined threshold, logs a file

## Usage
1. Clone the repository on your machine
2. Using Python 3, run the following command in the Linux terminal:
```
python3 /ScriptPath/PerformanceTracker.py
```
3. If no root directory is passed as an argument, the performance logs will be store in the PerformanceTracker.py directory

## Command and arguments
```
PerformanceTracker.py [-h] [-ct [[0-100]%]] [-mt [MBs]] [-ld [DIRECTORY]] [-pa [processAmount]]

optional arguments:
  -h, --help            show this help message and exit
  -ct [[0-100]%], --cputh [[0-100]%]
                        CPU usage percentage threshold. Default is 70
  -mt [MBs], --memth [MBs]
                        Memory usage MB threshold. Default is 3000 MB
  -ld [DIRECTORY], --logsdir [DIRECTORY]
                        Root directory for the logs to be stored. Ex: /home/userdir. Default is PerformanceTracker.py's directory
  -pa [processAmount], --pamount [processAmount]
                        Amount of processes to store in a log. Default is 5
```