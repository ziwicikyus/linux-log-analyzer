import argparse

FAILED_KEYWORDS = [
    "Failed password",
    "authentication failure",
    "invalid user"
]

def parse_args():
    parser = argparse.ArgumentParser(
        description="Linux Log Analyzer v0.2"
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )
    parser.add_argument(
        "--failed-only",
        action="store_true",
        help="Show only failed authentication attempts"
    )
    return parser.parse_args()

def analyze_log(file_path, failed_only):
    fail_count = 0
    output_count = 0  # Toplam yazdırılan satır sayısı

    try:
        with open(file_path, "r") as log_file:
            for line in log_file:
                line = line.strip()
                is_failed = any(k in line for k in FAILED_KEYWORDS)

                if is_failed:
                    fail_count += 1
                    print("[FAILED]", line)
                    output_count += 1
                else:
                    if not failed_only:
                        print(line)
                        output_count += 1

        print(f"\nTotal lines output: {output_count}")
        if failed_only:
            print(f"Total failed login attempts: {fail_count}")

    except FileNotFoundError:
        print("Error: Log file not found.")
    except PermissionError:
        print("Error: Permission denied.")

def main():
    args = parse_args()
    analyze_log(args.file, args.failed_only)

if __name__ == "__main__":
    main()
