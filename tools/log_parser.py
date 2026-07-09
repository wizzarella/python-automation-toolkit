"""
Parse a log file and count log levels. 

This script counts how many lines contain ERROR, WARNING and INFO
"""

import sys
from pathlib import Path


def parse_log_file(log_file):
  if not log_file.is_file():
    print("Error: log path is not a file")
    sys.exit(1)
  
  error_count = 0
  warning_count = 0
  info_count = 0

  for line in log_file.read_text().splitlines():
    if "ERROR" in line:
      error_count += 1
    elif "WARNING" in line:
      warning_count += 1
    elif "INFO" in line:
      info_count += 1

  print (f"Log file: {log_file}")
  print(f"ERROR: {error_count}")
  print(f"WARNING: {warning_count}")
  print(f"INFO: {info_count}")


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 tools/log_parser.py <log_file>")
    sys.exit(1)

  log_file= Path(sys.argv[1]).resolve()
  parse_log_file(log_file)

if __name__ == "__main__":
  main()
