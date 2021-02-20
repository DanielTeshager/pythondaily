#!/usr/bin/env python3
"""
This scrip tries to visualize the suronding sound by using a smart lamp. 
yeelight, sounddevice and numpy libraries are dependencies and need to be downloaded.

sounddevice - used to listen to environment audio throug the built in microphone.
numpy - used to analyse and manipulate the sound data captured through sounddevice
yeelight - to control my xiaomi lamp 

"""
import numpy as np
from yeelight import Bulb
import sounddevice as sd

#Initialize the lamp!
bulb = Bulb('192.168.0.198')
#Alternatively bulbs = yeelight.discover_bulbs() can be used to discover bulbs if you dont know the ip address of your bulb

#Enable bulbs music mode which removes the communication rate limit and allows you to 
#Send and reveive as many communication as needed.
bulb.start_music()

# Sample audio rate
fs = 44100  
# Duration of recording
seconds = 0.01 

try:
    while True:
        #record audio for x seconds
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1,blocking=True)

        #get the maximum value of the audio input using numpy max() function
        b = int((myrecording[:,0].max())*100)

        #set the max brightness value to 100 in the event we get a maxval that's greater than 100
        if b >= 100:
            b = 100

        #scale hue value between 0-359 by using the brightness value 
        h = int((b)/(100)*(359))
        
        #set hue,saturation,brighness value. Below saturation is set to 100 i.e. max saturation
        bulb.set_hsv(h,100,b)

        #print(h,maxval)
except KeyboardInterrupt:
    print('Interrupted')