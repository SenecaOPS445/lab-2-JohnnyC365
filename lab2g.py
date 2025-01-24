#!/usr/bin/env python3

import sys

# Author: Your Full Name
# Author ID: seneca_id
# Date Created: yyyy/mm/dd


if len(sys.argv) > 1:
    try:
        timer = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer for the timer.")
        sys.exit(1)
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
