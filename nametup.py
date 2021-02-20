#!/usr/bin/env python3
import re
from collections import namedtuple
n = int(input())
student,total = namedtuple('Student',input().split()), 0
for i in range(1,n):
    total+=float(student(*input().split()).MARKS)
print(total/n)
