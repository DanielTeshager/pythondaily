#!/usr/bin/env python3

from collections import Counter

shoes = int(input())
sizes = Counter(input().split())
customers = int(input())
total_price = []
for _ in range(customers):
    size, price = input().split()
    if sizes.get(size,0)!=0:
        total_price.append(float(price))
        sizes[size]=sizes.get(size,0)-1

print(sum(total_price))

