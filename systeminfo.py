#!/usr/bin/env python3

import re
import csv

with open('recent-grades.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    majors = {}
    for r in reader:
        majors[r['Major_category']]=majors.get(r['Major_category'],0)+1
    sorted_major = dict( sorted(majors.items(), key = lambda x: x[1], reverse=True))
    print(sorted_major,sep=",")