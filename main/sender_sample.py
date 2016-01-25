# Example of steganography in the video
# Using stepic to edit the frames from a video directly.

import cv2
import numpy as np
from PIL import Image
import stepic

cap = cv2.VideoCapture('sample1.avi')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIB ')

# generate all frames
frames = []
while True:
	ret, temp = cap.read()
	if not ret:
		break
	frames += [temp]

index = 42 # <- Index at which our data is hidden (frame no.)
fps = cap.get(cv2.CAP_PROP_FPS) # Framerate of o/p = i/p

# steganography on index frame
img = Image.fromarray(frames[index])
stegimg = stepic.encode(img, 'Index frame data to be encoded!')
frames[index] = np.array(stegimg)

# write image into video
h, w = frames[0].shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'DIB ')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

for each_frame in frames:
	out.write(each_frame)
