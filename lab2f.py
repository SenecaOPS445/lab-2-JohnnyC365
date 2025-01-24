#!/usr/bin/env python3

import sys

# Author: John Cherubini
# Author ID: jacherubini
# Date Created: 2025/01/24

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <starting_number>")
    sys.exit(1)

try:
    timer = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer for the timer.")
    sys.exit(1)

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
