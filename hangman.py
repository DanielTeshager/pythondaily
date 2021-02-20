#!/usr/bin/env python3

import random

lines =[]
with open('sopoddict.txt','r') as f:
    for i in range((267750//4)):
        lines.append(f.readline().strip())
print(random.sample(lines,2))