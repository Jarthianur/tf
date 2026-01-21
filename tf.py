#!/usr/bin/env python3
import sys
import re
import os.path

if len(sys.argv) < 2:
    print("Usage: {} <regex> <format>".format(os.path.basename(sys.argv[0])))
    exit(0)
try:
    r = re.compile(sys.argv[1])
except re.error as e:
    print("ERROR: {}".format(e), file=sys.stderr)
    exit(1)
f = "{}"
if len(sys.argv) > 2:
    f = sys.argv[2]
for line in sys.stdin:
    m = r.search(line)
    if m is None:
        continue
    try:
        print(f.format(*m.groups()))
    except Exception as e:
        print("ERROR: {}".format(e), file=sys.stderr)
        exit(1)
