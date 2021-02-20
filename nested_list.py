#!/usr/bin/env python3
import itertools
from itertools import islice

if __name__ == '__main__':
    motherlist =[]
    minscore = 0
    sminscore = 0
    minscorename = ""
    sminscorename = ""
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        childlist = []
        childlist.append(name)
        childlist.append(score)
       
        if len(motherlist)==0:
            minscore = score
            minscorename = name
            motherlist.append(childlist) 
        
        elif minscore > score:
            sminscore = minscore
            minscore = score
            sminscorename = minscorename
            miniscorename = name
        
        elif minscore == score:
            sminscorename = sminscorename if name > sminscorename else name
        
        motherlist.append(childlist)

    dic = dict(motherlist)
    dic = dict(sorted(dic.items(), key=lambda x: (x[1],x[0])))
    second_smallest = list(sorted(set(dic.values())))[1] if len(set(dic.values())) > 1 else dic.values()
    d = {k:v for k,v in dic.items() if v==second_smallest}
    for name in d.keys():
        print(name)