#!/usr/bin/python3
import random
import sys
from time import sleep
from datetime import datetime

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

for _ in range(10000):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    date = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    code = random.choice(status_codes)
    size = random.randint(1, 1024)
    log_line = '{} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(ip, date, code, size)
    sys.stdout.write(log_line)
    sys.stdout.flush()
    sleep(random.uniform(0, 0.1))