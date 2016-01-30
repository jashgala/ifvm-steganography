import cv2
import stepic
import numpy as np
from PIL import Image
from Crypto.Cipher import AES
import binascii

def decodeIndexHash(hash):
	dec_obj = AES.new('IFVM_STD_KEYCODE', AES.MODE_ECB) #same key as encrypter!!!
	frame_no_recv = dec_obj.decrypt(hash) #decryption at receiver end
	frame_no_int = int(frame_no_recv) #converting it to frameno from str
	print 'On decoding Hash, Frame number is:',frame_no_int
	return frame_no_int

if __name__ == '__main__':
	# code to test if steganography was successful
	cap = cv2.VideoCapture('output.avi')

	input_hash = raw_input('Enter the key for your data: ')
	index = int(decodeIndexHash(binascii.unhexlify(input_hash))) # <- Index at which our data is hidden

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