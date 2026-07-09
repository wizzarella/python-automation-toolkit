"""
Check host reachability using ping.

This script reads hosts from a text file and checks whether each host responds.
"""

import subprocess
import sys
from pathlib import Path


def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3,
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False


def check_hosts(hosts_file):
  if not hosts_file.is_file():
    print("Error: hosts path is not a file")
    sys.exit(1)
  
  hosts = hosts_file.read_text().splitlines()

  for host in hosts:
    host = host.strip()

    if not host:
      continue

    if ping_host(host):
      print(f"{host}: reachable")
    else:
      print(f"{host}: unreachable")


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 tools/ping_hosts.py <hosts_file>")
    sys.exit(1)

  hosts_file = Path(sys.argv[1]).resolve()
  check_hosts(hosts_file)

if __name__ == "__main__":
  main()
