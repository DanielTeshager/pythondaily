#!/usr/bin/env python3

val = input()
h,w = val.split(" ")
h,w= int(h),int(w)

mid = h//2
li = list(range(1,mid+1))
li_in = li[::-1]
li.append(0)
li.extend(li_in)
for i in li:
    if i!=0:
        print(((abs(i)*2-1)*'.|.').center(w,'-'))
    else:
        print('WELOCME'.center(w,'-')) 



#what works properly with elegance 
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))