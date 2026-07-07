"""
Analyze disk usage for a directory.

This script will count files, calculate total size, and find the largest file.
"""

from pathlib import Path


def analyze_directory(directory):
    print(f"Target directory: {directory}")

    if directory.is_dir():
        print("Ready to analyze directory")
        file_count = 0
        total_size = 0
        largest_file = None
        largest_size = 0

        for item in sorted(directory.iterdir()):
            if not item.is_file():
                continue

            file_count += 1
            print(item.name)

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

    else:
        print("Error: target path is not a directory")


target_directory = Path("examples/sample_directory").resolve()
analyze_directory(target_directory)