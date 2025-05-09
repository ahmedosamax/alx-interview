#!/usr/bin/python3
"""Reads from stdin and computes metrics"""
import sys

def print_stats(file_size, status_codes):
    """Prints the accumulated metrics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

file_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 7:
            try:
                code = parts[-2]
                size = int(parts[-1])
                file_size += size

                if code in valid_codes:
                    if code in status_codes:
                        status_codes[code] += 1
                    else:
                        status_codes[code] = 1

                line_count += 1
                if line_count == 10:
                    print_stats(file_size, status_codes)
                    line_count = 0
            except Exception:
                continue
except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise
finally:
    if line_count > 0:
        print_stats(file_size, status_codes)
