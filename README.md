# Python Automation Toolkit

A collection of small Python scripts for Cloud, Linux, and DevOps automation practice.

## Learning Focus

This repository is a hands-on learning project created to practice Python automation with the standard library.

The goal is not to build complex production tools, but to understand how small scripts can support Cloud, Linux, and DevOps workflows.

## Platform Note

The examples use `python3` and are intended for Linux/macOS terminal environments.

## Tools

### disk_usage.py

Analyzes a directory and shows:

- number of files
- total size in bytes
- largest file

Usage:

```bash
python3 tools/disk_usage.py examples/sample_directory
```

### log_parser.py

Analyzes a log file and counts log levels:

- ERROR
- WARNING
- INFO

Usage:

```bash
python3 tools/log_parser.py examples/sample.log
```

### backup_zip.py

Creates a zip backup from a source directory.

Usage:

```bash
python3 tools/backup_zip.py examples/sample_directory backups/sample_directory.zip
```

### ping_hosts.py

Reads a list of hosts from a text file and checks whether each host is reachable using `ping`.

Usage:

```bash
python3 tools/ping_hosts.py examples/hosts.txt
```

### port_checker.py

Checks whether one or more TCP ports are open on a target host.

Usage:

```bash
python3 tools/port_checker.py google.com 80 443 22
```

### password_generator.py

Generates a random password using letters, digits, and punctuation.

Usage:

```bash
python3 tools/password_generator.py 16
```

### csv_report.py

Reads a CSV file and generates a simple summary report.

The script shows:

- number of rows
- column names
- totals for numeric columns

Usage:

```bash
python3 tools/csv_report.py examples/cloud_costs.csv
```

### system_info.py

Displays basic information about the current system and Python runtime.

The script shows:

- operating system
- OS version
- machine architecture
- hostname
- current user
- current directory
- CPU count
- Python version

Usage:

```bash
python3 tools/system_info.py
```
