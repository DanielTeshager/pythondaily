#!/usr/bin/env python3
import sys
import cv2
import numpy as np


video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Video', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()