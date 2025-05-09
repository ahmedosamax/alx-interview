#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>, skip line if not this format
After every 10minutes or keyboard interrupt (CTRL + C)
print these from beginning: number of lines by status code
possible status codes: 200, 301, 400, 401, 404, 405, and 500
if status code isn't an integer, do not print it
format: <status code>: <number>
Status code must be printed in ascending order
"""

import sys
import signal
import re

total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        match = re.match(
            r'^(\d{1,3}\.){3}\d{1,3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
            line.strip()
        )
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))
            total_size += file_size
            if status_code in valid_status_codes:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
else:
    print_stats()
