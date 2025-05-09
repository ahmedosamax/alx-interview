#!/usr/bin/python3
"""Reads from stdin and computes metrics"""
import sys
import re

total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_counter = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(
            r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
            line
        )
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total_size += file_size
            if status_code in valid_codes:
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1
            line_counter += 1
            if line_counter % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    if line_counter % 10 != 0:
        print_stats()
