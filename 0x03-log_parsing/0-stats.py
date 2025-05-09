#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """Print the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL+C)"""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            # Parse the line
            parts = line.split()
            if len(parts) < 9:
                continue
            
            # Extract file size and status code
            ip = parts[0]
            date = parts[3] + " " + parts[4]
            method = parts[5]
            path = parts[6]
            protocol = parts[7]
            status_code = parts[8]
            file_size = parts[9]
            
            # Validate the format
            if (method != '"GET' or path != '/projects/260' or 
                protocol != 'HTTP/1.1"'):
                continue
                
            # Update metrics
            try:
                status_code = int(status_code)
                file_size = int(file_size)
                
                if status_code in status_counts:
                    total_size += file_size
                    status_counts[status_code] += 1
                    line_count += 1
            except ValueError:
                continue
                
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()
                
        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    raise

# Print any remaining stats at the end
print_stats()