# Linux Log Analyzer v0.2

## status
Early development (v0.2)

# A simple and practical python based CLI tool for analyzing Linux log files and detecting potencial brute force attacks.
# Version 0.2 allows you to filter only failed login attempts and see the total fail count. 
 

 'I added some stuff on log file to make sure that the script can actually reads the file and gives me the output that i seek.'

## Features – v0.2
- select the log file via CLI (`--file`)
- filter failed authentication attempts (`--failed-only`)
- display the total number of failed attempts
- view all log entries if fail filter is not applied

## Requirements
- Python 3.x
- access permission for the log fie


## Installation
1. Clone the repository or download the zip:

   git clone https://github.com/ziwicikyus/linux-log-analyzer.git




Features

- detects how many log attempts have exists. (v0.1)
- select the log file via CLI (`--file`) (v0.2)
- filter failed authentication attempts (`--failed-only`) (v0.2)
- display the total number of failed attempts (v0.2)
- view all log entries if fail filter is not applied (v0.2)


if there is no such a log file, it automaticly warns the user.

Usage

*make sure u delete the example logs that i have wrote on the log file before u actually use the tool. They are only examples and not for real use*



Windows: PowerShell

Linux: Terminal



View all log entries:

python analyzer.py --file /path/to/logfile.log


View only failed log entries + total fail count: 

python analyzer.py --file /path/to/logfile.log --failed-only


Windows path example:

& C:/Users/user/AppData/Local/Programs/Python/Python314/python.exe C:/Users/user/Desktop/linux-log-analyzer/analyzer.py --file C:/Users/user/Desktop/linux-log-analyzer/logs/auth.log --failed-only





Output Example – Fail Only
[FAILED] Failed password for root from 192.168.1.10
[FAILED] Failed password for admin from 192.168.1.11

Total lines output: 2
Total failed login attempts: 2




Output Example – All Log Entries
Line1
Line2
[FAILED] Failed password for root from 192.168.1.10
Line4
...

Total lines output: X



Purpose


I created this tool for gaining experience in log analysis, basic detection logic and being familiar with SOC style thinking.
