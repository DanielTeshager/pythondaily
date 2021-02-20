#!/usr/bin/env python3

"""
This script utilizes pyautogui library's position and pixel method
to read the current position and pixel color value in RGB of the mouse pointer 
and set the color of yeelamp connected to my lan.
"""

import pyautogui
import sys
import re
from yeelight import Bulb
import time

#create a lamp instance
b = Bulb('192.168.0.198')

print('Press Ctrl-C to quit.')
try:
    while True:
        #get the x,y coordinate of the mouse pointer
        x, y = pyautogui.position()

        #make it nice and printable 
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        #get the color value of the pixel under the current mouse pointer
        color = str(pyautogui.pixel(x,y))

        #print(color,type(color))

        #use regular expression to find the color value fromated as RGB(red=ddd, green=ddd, blue=ddd)
        red,green,blue=tuple([int(x) for x in re.findall(r"=(\d{1,})",color)])
        #print('\b' * 100, end='', flush=True)

        #set the lamps rgb value based the current position of the mouse pointer
        b.set_rgb(red,green,blue)
        time.sleep(3)

#allows to close the program by pressing Ctrl-c
except KeyboardInterrupt:
    print('\n')