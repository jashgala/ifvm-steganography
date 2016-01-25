import cv2
import stepic
import numpy as np
from PIL import Image

# code to test if steganography was successful
cap = cv2.VideoCapture('output.avi')
index = 42 # <- Index at which our data is hidden
frames = []
while True:
	ret, temp = cap.read()
	if not ret:
		break
	frames += [temp]

print "Length of frames read from output: ",len(frames)
img = Image.fromarray(frames[index])
hiddenmsg = stepic.decode(img).decode()
print hiddenmsg