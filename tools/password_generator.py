"""
Generate a random password.

This script creates a password using letters, digits, and punctuation.
"""

import secrets
import string
import sys


def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ""

  for _ in range(length):
    password += secrets.choice(characters)
  
  return password


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/password_generator.py <length>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Error: length must be a number")
        sys.exit(1)

    if length < 8:
        print("Error: length must be at least 8")
        sys.exit(1)

    password = generate_password(length)
    print(f"Generated password: {password}")


if __name__ == "__main__":
  main()
