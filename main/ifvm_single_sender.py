# Example of steganography in the video
# Using stepic to edit the frames from a video directly.

import cv2
import numpy as np
from PIL import Image
import stepic
import random

def generateRandomFrameNo(frameCount, occ):
	''' Generates random frame number taking into account the occupied frames. '''
	while (True):
		ret = random.randrange(0, frameCount, 1)
		if ret not in occ: return ret


def generateIndexData(filename, paramStr):
	return filename.split('.')[1] + ';' + paramStr + ';'

cap = cv2.VideoCapture('sample1.avi')
frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print frameCount 
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIB ')

# generate all frames
frames = []
while True:
	ret, temp = cap.read()
	if not ret:
		break
	frames += [temp]

# selecting an index frame
occ = [] # <- currently no frames will be occupied
index = generateRandomFrameNo(frameCount, occ) # <- Index at which our data is hidden (frame no.)
print 'Index frame no: ', index
occ += [index]

# generating data that will be encoded in index frame
indexData = generateIndexData('abc.java','')

# generaing data frame
data1Loc = generateRandomFrameNo(frameCount, occ)
indexData += str(data1Loc) + ','
data1 = 'Data 1 is the name Jash'

data2Loc = generateRandomFrameNo(frameCount, occ)
indexData += str(data2Loc)
data2 = 'Data 2 is the name VJTI'

# steganography on index frame
img = Image.fromarray(frames[index])
stegimg = stepic.encode(img, indexData)
frames[index] = np.array(stegimg)

# steganography on data frame 1
img = Image.fromarray(frames[index])
stegimg = stepic.encode(img, data1)
frames[data1Loc] = np.array(stegimg)

# steganography on data frame 2
img = Image.fromarray(frames[index])
stegimg = stepic.encode(img, data2)
frames[data2Loc] = np.array(stegimg)

# write image into video
h, w = frames[0].shape[:2]
fps = cap.get(cv2.CAP_PROP_FPS) # Framerate of o/p = i/p
fourcc = cv2.VideoWriter_fourcc(*'DIB ')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

for each_frame in frames:
	out.write(each_frame)

print 'Steganography done. Look for output.avi'