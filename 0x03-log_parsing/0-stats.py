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
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        match = re.match(
            r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
            line.strip()
        )
        if match:
            code, size = match.group(1), match.group(2)
            total_size += int(size)
            if code in valid_codes:
                status_counts[code] = status_counts.get(code, 0) + 1
            line_counter += 1
            if line_counter % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    if line_counter % 10 != 0:
        print_stats()
