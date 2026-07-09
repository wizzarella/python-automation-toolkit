"""
Display basic system information. 

This script prints useful details about the operating system, machine, user, current directory, CPU count, and Python runtime.
"""

import getpass
import os
import platform
import socket
import sys
from pathlib import Path


def show_system_info():
  print("System information:")
  print(f"OS: {platform.system()}")
  print(f"OS version: {platform.version()}")
  print(f"Machine: {platform.machine()}")
  print(f"Hostname: {socket.gethostname()}")
  print(f"Current user: {getpass.getuser()}")
  print(f"Current directory: {Path.cwd()}")
  print(f"CPU count: {os.cpu_count()}")
  print(f"Python version: {sys.version.split()[0]}")


def main():
  show_system_info()


if __name__ == "__main__":
  main()
