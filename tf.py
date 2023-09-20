#!/usr/bin/env python3
import sys
import re

if len(sys.argv)!= 3:
    print("Usage: {} <regex> <format>".format(sys.argv[0]))
    exit(0)
try:
    r=re.compile(sys.argv[1])
except re.error as e:
    print( "ERROR: {}".format(e),file=sys.stderr)
    exit(1)
f=sys.argv[2]
for line in sys.stdin:
    m = r.search(line)
    if m is None:
        continue
    try:
        print(f.format(*m.groups()))
    except Exception as e:
        print("ERROR: {}".format(e),file=sys.stderr)
        exit(1)
