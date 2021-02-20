#!/usr/bin/env python3
string = 'BANANA'
vowel =['A','E','I','O','U']
S=0
K=0
for i in range(len(string)):
    if string[i] in vowel:
        K+= len(string)-i
    else:
        S+=len(string)-i
        print(S)
if S>K:
    print("Stuart"+" "+ "%d" % S)
elif K>S:
    print("Kevin"+" "+'%d' % K)
else:
    print("Draw")