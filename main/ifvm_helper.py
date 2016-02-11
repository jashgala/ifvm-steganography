import cv2
import numpy as np
from PIL import Image
import stepic
import random
import os
from Crypto.Cipher import AES
import binascii

def generateRandomFrameNo(frameCount, occ):
	''' Generates random frame number taking into account the occupied frames. '''
	while (True):
		ret = random.randrange(0, frameCount, 1)
		if ret not in occ: 
			occ += [ret]
			return ret

def generateIndexHash(frame_number):
	enc_obj = AES.new('IFVM_STD_KEYCODE', AES.MODE_ECB) #note that key must be 16x chars
	string_to_encrypt = str(frame_number).zfill(16) #padding to make message size 16x
	generated_hash = enc_obj.encrypt(string_to_encrypt) #encryption to generate the hash
	key = binascii.hexlify(generated_hash)
	print key
	return key

def decodeIndexHash(hash):
	dec_obj = AES.new('IFVM_STD_KEYCODE', AES.MODE_ECB) #same key as encrypter!!!
	frame_no_recv = dec_obj.decrypt(hash) #decryption at receiver end
	frame_no_int = int(frame_no_recv) #converting it to frameno from str
	print 'On decoding Hash, Frame number is:',frame_no_int
	return frame_no_int

def generateIndexData(filename, paramStr):
	return filename.split('.')[1] + ';' + paramStr + ';'

def getAllFrames(cap):
	frames = []
	while True:
		ret, temp = cap.read()
		if not ret:
			break
		frames += [temp]
	return frames

def generateTextBlocks(filename, byteCapacity):
	f = open(filename, 'r')
	blocks = []
	while True:
		currBlock = f.read(byteCapacity)
		if currBlock == '': break
		blocks += [currBlock]
	return blocks


def writeToVideo(frames, output_path, fps):
	h, w = frames[0].shape[:2]
	fourcc = cv2.VideoWriter_fourcc(*'DIB ')
	out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))
	for each_frame in frames:
		out.write(each_frame)