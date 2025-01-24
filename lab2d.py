#!/usr/bin/env python3

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    # Use exit code 0 for normal script termination when showing usage
    sys.exit(0)

# Assign command-line arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Ensure the age is a valid integer
try:
    age = int(age)
except ValueError:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Use exit code 0 to gracefully handle invalid input

# Print the output with the exact required formatting
print(f"Hi {name}, you are {age} years old.")
