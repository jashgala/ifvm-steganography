import cv2
import numpy as np

cap = cv2.VideoCapture('sample1.avi')

ret, frame = cap.read()

first = True
while ret != 0:
    ret, frame = cap.read()
    if first:
        h,w = frame.shape[:2]
        writer = cv2.VideoWriter(filename="res.avi", fourcc=cv2.VideoWriter_fourcc('D','I','B',' '), fps=30, frameSize=(w,h))
        first = False
    c+=1
    if c>50 and c<100:
   	    frame[0,0] = 50
    writer.write(frame)