#!/usr/bin/python3
import sys
from collections import Counter

count = {}
for line in sys.stdin:
    line = line.split('\t')
    try:
        count[line[0]] += 1
    except:
        count[line[0]] = 1 
    print('Top10Artists\tCount')
    count = Counter(count).most_common(10)
for (key, value) in count:
    print('{}\t{}'.format(key, value))