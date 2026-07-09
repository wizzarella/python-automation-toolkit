"""
Create a zip backup of a directory.

This script compresses a source directory into a zip file.
"""

import sys
import zipfile
from pathlib import Path


def create_zip_backup(source_directory, output_zip):
  if not source_directory.is_dir():
    print("Error: source path is not a directory")
    sys.exit(1)

  output_zip.parent.mkdir(parents=True, exist_ok=True)

  with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for item in source_directory.rglob("*"):
      if item.is_file():
        archive_name = item.relative_to(source_directory)
        zip_file.write(item, archive_name)
  
  print(f"Backup created:{output_zip}")


def main():
  if len(sys.argv) < 3:
    print("Usage: python3 tools/backup_zip.py <source_directory> <output_zip>")
    sys.exit(1)
  
  source_directory = Path(sys.argv[1]).resolve()
  output_zip = Path(sys.argv[2]).resolve()

  create_zip_backup(source_directory, output_zip)


if __name__ == "__main__":
  main()
