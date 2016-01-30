import cv2
import numpy as np
from PIL import Image
import stepic
import random

from Crypto.Cipher import AES
import binascii

def generateRandomFrameNo(frameCount, occ):
	''' Generates random frame number taking into account the occupied frames. '''
	while (True):
		ret = random.randrange(0, frameCount, 1)
		if ret not in occ: 
			occ += [ret]
			return ret


def generateIndexData(filename, paramStr):
	return filename.split('.')[1] + ';' + paramStr + ';'

def generateTextBlocks(filename, byteCapacity):
	f = open(filename, 'r')
	blocks = []
	while True:
		currBlock = f.read(byteCapacity)
		if currBlock == '': break
		blocks += [currBlock]
	return blocks

def generateIndexHash(frame_number):
	enc_obj = AES.new('IFVM_STD_KEYCODE', AES.MODE_ECB) #note that key must be 16x chars
	string_to_encrypt = str(frame_number).zfill(16) #padding to make message size 16x
	generated_hash = enc_obj.encrypt(string_to_encrypt) #encryption to generate the hash
	print binascii.hexlify(generated_hash)

def stegoTextBlocks(frames, occ, blocks):
	index = generateRandomFrameNo(len(frames), occ) # <- Index at which our data is hidden (frame no.)
	print 'Index frame no: ', index

	generateIndexHash(index) # generate and print hash code to use as key

	# generating data that will be encoded in index frame
	indexData = generateIndexData('file1.txt','')

	for block in blocks:
		loc = generateRandomFrameNo(len(frames), occ)
		indexData += str(loc) + '.'
		img = Image.fromarray(frames[index])
		stegimg = stepic.encode(img, block)
		frames[loc] = np.array(stegimg)
		
	# steganography on index frame
	print 'Index Frame Data: ', indexData
	img = Image.fromarray(frames[index])
	stegimg = stepic.encode(img, indexData)
	frames[index] = np.array(stegimg)

### MAIN PROGRAM ###
cap = cv2.VideoCapture('sample1.avi')
frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print frameCount 

# generate all frames
frames = []
while True:
	ret, temp = cap.read()
	if not ret:
		break
	frames += [temp]

# define capacity of each data frame
h, w = frames[0].shape[:2]
pixelCount = h * w - 1
byteCapacity = pixelCount / 9 # defines maximum no. of bytes that can be stored in an image (Ref. http://domnit.org/blog/2007/02/stepic-explanation.html)

print byteCapacity

occ = [] # <- currently no frames will be occupied

blocks = generateTextBlocks('file1.txt', byteCapacity)
stegoTextBlocks(frames, occ, blocks)

# write image into video
h, w = frames[0].shape[:2]
fps = cap.get(cv2.CAP_PROP_FPS) # Framerate of o/p = i/p
fourcc = cv2.VideoWriter_fourcc(*'DIB ')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

for each_frame in frames:
	out.write(each_frame)

print 'Steganography done. Look for output.avi'