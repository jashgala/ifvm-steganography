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
import multi_text_sender
import Image_on_image as ioi

# To keep track of occupied frames
occ = []

def main():
	cover_video = 'drop.avi'
	secret_img_path = 'Desitakes.jpg'
	cap = cv2.VideoCapture(cover_video)
	frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	fps = cap.get(cv2.CAP_PROP_FPS) # Framerate of o/p = i/p
	frames = getAllFrames(cap)
	sliceAndEmbed(frames, secret_img_path, occ)
	writeToVideo(frames,'output.avi', fps)

def getAllFrames(cap):
	frames = []
	while True:
		ret, temp = cap.read()
		if not ret:
			break
		frames += [temp]
	return frames

def sliceAndEmbed(frames, secret_img_path, occ):
	''' Partitions secret image into smaller images and embeds them in cover video '''
	secret_img = Image.open(secret_img_path)
	frame_h, frame_w = frames[0].shape[:2]
	secret_h, secret_w = secret_img.size[1], secret_img.size[0]
	# Temporarily(& Arbritrarily) setting max slice size as 1 sixth of cover image
	max_h, max_w = frame_h/6, frame_w/6
	numberOfSlices = ceil(secret_h/max_h)*ceil(secret_w/max_w)
	tiles = image_slicer.slice(secret_img_path, numberOfSlices, save=False)

	# Rough Index data for now
	indexData = str(secret_img.size[0]) + ";" + str(secret_img.size[1]) + ";" 
	indexData+= str(len(tiles)) + ";" + str(tiles[0].image.size[0]) + ';' + str(tiles[0].image.size[1]) + '.'
	index = multi_text_sender.generateRandomFrameNo(len(frames), occ)
	for i in tiles:
		loc = multi_text_sender.generateRandomFrameNo(len(frames), occ)
		indexData += str(loc) + '.'
		cover_img = Image.fromarray(frames[loc])
		temp = ioi.hide_image(cover_img, i.image)
		frames[loc] = np.array(temp)

	# Index
	cover_img = Image.fromarray(frames[index])
	temp = ioi.hide_image(cover_img, i.image)
	frames[index] = np.array(temp)
	return frames

def writeToVideo(frames, output_path, fps):
	h, w = frames[0].shape[:2]	


if __name__ == '__main__':
	main()