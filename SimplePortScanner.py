#!/bin/python3
# Practical Ethical Hacking - The Complete Course
# Lesson by TCM Security, Inc., Heath Adams (Udemy)
# Implementing a super simple port scanner in Py3
# 1 thread, 1 speed :)
# Syntax: python3 scanner.py <ip>

import socket
import sys
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # 0 is script file name
else:
    print("Invalid amount af arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))  # current datetime to string
print("-" * 50)

try:
    for port in range(50, 60):  # Or (0,65535) for all ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
