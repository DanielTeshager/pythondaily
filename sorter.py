#!/usr/bin/env python3

row, col = list(map(int, input().split()))

arr,s = [],[]
for _ in range(row):
    arr.append(list(map(int, input().rstrip().split())))
key = int(input())
arr=sorted(arr, key=lambda x:x[key])
for a in arr:
    print(a)

