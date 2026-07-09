"""
Check whether TCP ports are open on a host.

This script tries to connect to one or more ports on a target host.
"""

import socket
import sys


def check_port(host, port):
  try:
    with socket.create_connection((host,port), timeout=3):
      return True
  except OSError:
    return False
  

def main():
  if len(sys.argv) < 3:
    print("Usage: python3 tools/port_checker.py <host> <port> [port...]")
    sys.exit(1)

  host = sys.argv[1]
  ports = sys.argv[2:]

  for port_text in ports:
    try:
      port = int(port_text)
    except ValueError:
      print(f"{port_text}: invalid port")
      continue

    if check_port(host,port):
      print(f"{host}:{port} open")
    else:
      print(f"{host}:{port} closed")


if __name__ == "__main__":
  main()