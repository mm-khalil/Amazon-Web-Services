#! /usr/bin/python3
import json
import sys
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    obj = json.loads(line)
    if obj['artist']:
    print('{}\t{}'.format(obj['artist'], 1))