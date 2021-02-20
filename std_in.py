#!/usr/bin/env python3
from itertools import islice

f = open('test.txt','r')
lines = f.read()
print(len(lines))
letters_dict = {}


for i in lines:
    letters_dict[i]=letters_dict.get(i,0)+1
final = dict(sorted(letters_dict.items(), key=lambda x: (-x[1],x[0])))
final  = dict(islice(final.items(),3))
for key, val in final.items():
    print(key,val)

f.close()

import string
