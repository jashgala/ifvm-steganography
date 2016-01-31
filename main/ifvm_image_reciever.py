import cv2
import numpy as np
from PIL import Image
import stepic
import random
from math import ceil, floor
from Crypto.Cipher import AES
import binascii
import image_slicer
# Temporary.. Need to consolidate all the common functions in a single file
import multi_text_receiver
import Image_on_image as ioi

def main():
	cap = cv2.VideoCapture('drop.avi')
	# input_hash = raw_input('Enter the key for your data: ')
	# index = int(multi_text_receiver.decodeIndexHash(binascii.unhexlify(input_hash))) # <- Index at which our data is hidden
	index = 4
	frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	frames = getAllFrames(cap)
	secret_img = extract(frames, index)


def getAllFrames(cap):
	frames = []
	while True:
		ret, temp = cap.read()
		if not ret:
			break
		frames += [temp]
	return frames

def reassemble_image(t, slice_size = (73,73), rows = 2, cols = 2):
    tiles = [] # The tiles of the image to be assembled
    number = 0
    for j in range(0,rows):
        for i in range(0,cols):
            coord_x = i*slice_size[0]
            coord_y = j*slice_size[1]
            coords = (coord_x, coord_y)
            position = (i+1,j+1)
            tile = image_slicer.Tile(t[number], number, position, coords)
            tiles.append(tile)
            number+=1
    res = image_slicer.join(tuple(tiles))
    return res

def extract(frames, index):
	img = Image.fromarray(frames[index])
	indexData = stepic.decode(img).decode()
	indexData = indexData.split('.')
	metaData = indexData[0].split(';')
	secret_img_size = (int(metaData[0]), int(metaData[1]))
	noOfTiles = int(metaData[2])
	slice_size = (int(metaData[3]), int(metaData[4]))
	t = []
	for i in range(1,len(indexData)):
		temp = frames[int(i)]
		res = ioi.extract_image(Image.fromarray(temp)).resize((slice_size[0], slice_size[1]))
		t.append(res)
	extracted_image = reassemble_image(t, slice_size, secret_img_size[0]/slice_size[0], secret_img_size[1]/slice_size[1])
	return extracted_image

if __name__ == '__main__':
	main()