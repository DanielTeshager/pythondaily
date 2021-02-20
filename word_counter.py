#!/usr/bin/env python3
from collections import OrderedDict
n = int(input())
wordlist = []
for _ in range(n):
    wordlist.append(input())
count = []
for word in OrderedDict.fromkeys(wordlist)):
    count.append(wordlist.count(word))

print(len(count))
print(*count)

# worddict = {}
# newwordlist = []
# y=
# # for word in wordlist:
# #     if word not in newwordlist:
# #         newwordlist.append(word)
# #         worddict[word] = wordlist.count(word)
# # print(len(worddict.values()))
# # print(*worddict.values())
# print(y)