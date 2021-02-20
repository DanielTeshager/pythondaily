#!/usr/bin/env python3

#prompt user to choose password strength 1, weak 2, stong

#Weak password will have char length 8 will have at least one caps and a numbers

#Strong password will have char length 25 will have caps, numbers and special chars

#define constant varibles
import random

W_PASSWROD_LEN = 8
S_PASSWOORD_LEN = 25
charlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,36, 64, 33, 35, 95, 37, 40, 41, 42, 65, 66, 67, 68, 69, 
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 
            98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
            116, 117, 118, 119, 120, 121, 122]

strength = int(input("Select your password strength 0 for week and 1 for strong default(0)") or "0")
if strength == 0:
    #print("Here's your weak ass password")
    sampleweak = random.sample(charlist,8)
    weakpassword = ''.join( [str(chr(x)) if x not in range(0,10) else str(x) for x in sampleweak] )
    #print("{} computer generated weak password ord".format(sampleweak))
    print("{} is a {} characters long computer generated weak password: ".format(weakpassword, len(weakpassword))) 
else:
    #print("Here's your badass stong password")
    samplestrong = random.sample(charlist,25)
    strongpassword = ''.join( [str(chr(x)) if x not in range(0,10) else str(x) for x in samplestrong] )
    #print("{} computer generated weak password ord".format(samplestrong,25))
    print("{} is a {} characters long computer generated strong password: ".format(strongpassword, len(strongpassword)))