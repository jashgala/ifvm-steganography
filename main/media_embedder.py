import cv2
import numpy as np
from PIL import Image
import stepic
import random
from math import ceil, floor
from Crypto.Cipher import AES
import binascii
import sys
import os
import base64
import ifvm_helper as ifvm

def main():
	occ = []
	cover = sys.argv[1]
	secret = sys.argv[2]
	embed(cover, secret, occ)

def embed(cover, secret, occ, saveLocation = "output.avi"):
	'''Embeds  images. Call this function when the module is imported
	cover = Cover Video Path/Location
	secret = secret Media Path/Location
	occ = List of occupied frames'''

	# Opening video & extracting frames
	cap = cv2.VideoCapture(cover)
	frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	fps = cap.get(cv2.CAP_PROP_FPS)
	frames = ifvm.getAllFrames(cap)

	# Opening secret Image and converting to string for embedding
	secret_media_text_file_path = "secret_file_154861.txt"
	with open(secret, "rb") as mediaFile:
		media_data = base64.b64encode(mediaFile.read())

	with open(secret_media_text_file_path, "w") as txt:
		txt.write(media_data)

	# define capacity of each data frame
	h, w = frames[0].shape[:2]
	pixelCount = h * w - 1
	byteCapacity = pixelCount / 9 # defines maximum no. of bytes that can be stored in an image (Ref. http://domnit.org/blog/2007/02/stepic-explanation.html)

	blocks = ifvm.generateTextBlocks(secret_media_text_file_path, byteCapacity)
	os.remove(secret_media_text_file_path)
	index = ifvm.generateRandomFrameNo(len(frames), occ)
	key = ifvm.generateIndexHash(index)

	# generating data that will be encoded in index frame
	indexData = ifvm.generateIndexData('output.txt', secret.split('.')[-1])

	for block in blocks:
		loc = ifvm.generateRandomFrameNo(len(frames), occ)
		indexData += str(loc) + '.'
		img = Image.fromarray(frames[loc])
		stegimg = stepic.encode(img, block)
		frames[loc] = np.array(stegimg)

	# steganography on index frame
	print 'Index Frame Data: ', indexData
	img = Image.fromarray(frames[index])
	stegimg = stepic.encode(img, indexData)
	frames[index] = np.array(stegimg)
	ifvm.writeToVideo(frames, saveLocation, fps)

if __name__ == '__main__':
	main()