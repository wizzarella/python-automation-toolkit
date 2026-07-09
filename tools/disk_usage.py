"""
Analyze disk usage for a directory.

This script counts files, calculates total size,
and finds the largest file in a directory.
"""

import sys
from pathlib import Path


def analyze_directory(directory):
    print(f"Target directory: {directory}")

    if not directory.is_dir():
        print("Error: target path is not a directory")
        sys.exit(1)

    file_count = 0
    total_size = 0
    largest_file = None
    largest_size = 0

    for item in sorted(directory.iterdir()):
        if not item.is_file():
            continue

        file_count += 1
        file_size = item.stat().st_size
        total_size += file_size

        if file_size > largest_size:
            largest_file = item
            largest_size = file_size

    print(f"Number of files: {file_count}")
    print(f"Total size: {total_size} bytes")

    if largest_file is None:
        print("Largest file: none")
    else:
        print(f"Largest file: {largest_file.name} ({largest_size} bytes)")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/disk_usage.py <directory>")
        sys.exit(1)

    target_directory = Path(sys.argv[1]).resolve()
    analyze_directory(target_directory)


if __name__ == "__main__":
    main()
