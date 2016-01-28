import cv2
import stepic
import numpy as np
from PIL import Image

# code to test if steganography was successful
cap = cv2.VideoCapture('output.avi')

inputNo = raw_input('Enter the frame no: ')
index = int(inputNo) # <- Index at which our data is hidden

frames = []

while True:
	ret, temp = cap.read()
	if not ret:
		break
	frames += [temp]

img = Image.fromarray(frames[index])
indexData = stepic.decode(img).decode()

indexData = indexData.split(';')
print 'File extension: ', indexData[0]

dataLocs = indexData[2].split(',')
data1Loc = int(dataLocs[0])
data2Loc = int(dataLocs[1])

img = Image.fromarray(frames[data1Loc])
data1 = stepic.decode(img).decode()
print 'Data 1: ' , data1

img = Image.fromarray(frames[data2Loc])
data2 = stepic.decode(img).decode()
print 'Data 2: ' , data2