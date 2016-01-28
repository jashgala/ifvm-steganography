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

f = open('outfile.' + indexData[0], 'w')

print 'File extension: ', indexData[0]

dataLocs = indexData[2].split('.')

for loc in dataLocs:
	if loc == '': break
	img = Image.fromarray(frames[int(loc)])
	block = stepic.decode(img).decode()
	f.write(block)

print 'Wrote file. Check \'outfile.txt\''