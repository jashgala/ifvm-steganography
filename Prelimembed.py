import cv2
import numpy as np

cap = cv2.VideoCapture('flame.avi')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
ret, frame = cap.read()
width = np.size(frame, 1)
height = np.size(frame, 0)

writer = cv2.VideoWriter(filename="res.avi", fourcc=cv2.VideoWriter_fourcc('I', 'Y', 'U', 'V'), fps=30, frameSize=(width, height))

c = 0
while ret != 0:
        ret, frame = cap.read()
       	# frame[0,0] = 1
       	# starting frames are empty.
       	# that counter is to be removed after we figure out how to detect the empty frames and deselect them
       	c+=1
       	if c>50 and c<100:
   			frame[0,0] = 50
        writer.write(frame)
