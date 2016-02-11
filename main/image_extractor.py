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
	cover = sys.argv[1]
	input_hash = raw_input('Enter the key for your data: ')
	extract(cover, input_hash)

def extract(cover, key):
	cap = cv2.VideoCapture(cover)
	index = int(ifvm.decodeIndexHash(binascii.unhexlify(key))) # <- Index at which our data is hidden

	frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	frames = ifvm.getAllFrames(cap)

	img = Image.fromarray(frames[index])
	indexData = stepic.decode(img).decode()
	indexData = indexData.split(';')

	img_txt_location = 'outfile.' + indexData[0]
	img_location = 'extractedImage.' + indexData[1]

	f = open(img_txt_location, 'w')

	dataLocs = indexData[2].split('.')

	for loc in dataLocs:
		if loc == '': break
		img = Image.fromarray(frames[int(loc)])
		block = stepic.decode(img).decode()
		f.write(block)
	f.close()

	with open(img_txt_location,"rb") as res:
		str = base64.b64decode(res.read())
	fh = open(img_location, "wb")
	fh.write(str)
	fh.close()
	os.remove(img_txt_location)


if __name__ == '__main__':
	main()