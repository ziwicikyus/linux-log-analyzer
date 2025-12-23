log_file = "logs/auth.log"

try:
    with open(log_file, "r", errors="ignore") as f:
        lines = f.readlines()
        print(f"Log file opened successfully. Total lines: {len(lines)}")
except FileNotFoundError:
    print("Log file not found.")

