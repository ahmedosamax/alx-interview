#!/usr/bin/python3
import random
import sys
from time import sleep
from datetime import datetime

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

for _ in range(10000):
    ip = "{}.{}.{}.{}".format(
        random.randint(1, 255), random.randint(1, 255),
        random.randint(1, 255), random.randint(1, 255)
    )
    date = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
    code = random.choice(status_codes)
    size = random.randint(1, 1024)

    line = '{} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(
        ip, date, code, size
    )
    sys.stdout.write(line)
    sys.stdout.flush()
    sleep(0.01)  # Slight delay to simulate real stream
