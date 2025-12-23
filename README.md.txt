# Linux Log Analyzer

A Python-based tool for analyzing Linux authentication logs to detect failed login attempts and potential brute force attacks.

 Purpose
This project was created to gain experience with:
- Log analysis
- Basic detection logic
- Blue team / SOC-style thinking

In this first v0.1 realese, my main focus was on the script if it actually can read the files and gives the output that I seek for.

 Features
- Parses Linux auth.log files
- Detects failed SSH login attempts
- Counts attempts per IP address
- Flags suspicious IPs based on a configurable threshold
- Exports results to a CSV report

 Project Structure
linux-log-analyzer/
├── analyzer.py
├── logs/
│ └── auth.log
├── failed_login_report.csv
└── README.md

 How It Works
1. Reads authentication logs line by line
2. Identifies failed login entries
3. Extracts source IP addresses
4. Counts repeated attempts
5. Flags IPs exceeding the defined threshold
6. Generates a CSV report for further analysis

CSV report:
- IP Address
- Failed Attempts
- Alert status (YES / NO)

  What I Learned
- How authentication failures appear in real logs
- Basic brute force detection logic
- Turning raw log data into actionable reports
- Thinking like a SOC analyst rather than just writing scripts

 Possible Improvements
- Time-based analysis (night-time activity detection)
- Username-based correlation
- Integration with real SIEM tools
- Automated blocking (Fail2Ban-style logic)

 Disclaimer
This project is for educational purposes only and was tested in a controlled environment.