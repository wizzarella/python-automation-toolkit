"""
Generate a simple report from a CSV file. 

This script read cloud service costs and prints a summary.
"""

import csv
import sys 
from pathlib import Path


def generate_report(csv_file):
  if not csv_file.is_file():
    print("Error: CSV path is not a file")
    sys.exit(1)

  total_cost = 0
  row_count = 0
  highest_service = None
  highest_cost = 0

  with csv_file.open(newline="") as file:
    reader = csv.DictReader(file)

    if "service" not in reader.fieldnames or "cost" not in reader.fieldnames:
      print("Error: CSV must contain 'service' and 'cost' columns")
      sys.exit(1)
    
    for row in reader:
      service = row["service"]
      cost = float(row["cost"])

      row_count += 1
      total_cost += cost

    if cost > highest_cost:
      highest_service = service
      highest_cost = cost

  print(f"CSV file: {csv_file}")
  print(f"Rows: {row_count}")
  print(f"Total cost: {total_cost:.2f}")
  print(f"Highest cost: {highest_service} ({highest_cost:.2f})")


def main():
  if len(sys.argv) < 2:
    print("Usage:python3 tools/csv_report.py <csv_file>")
    sys.exit(1)

  csv_file = Path(sys.argv[1]).resolve()
  generate_report(csv_file)


if __name__ == "__main__":
  main()



