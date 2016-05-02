from __future__ import print_function

import cv2
import sys
import ifvm_helper as ifvm
import math

def main():
	cover = sys.argv[1]
	stego = sys.argv[2]
	cover = cv2.VideoCapture(cover)
	stego = cv2.VideoCapture(stego)

	frameCount = int(cover.get(cv2.CAP_PROP_FRAME_COUNT))
	cover_frames = ifvm.getAllFrames(cover)
	stego_frames = ifvm.getAllFrames(stego)

	mse = 0.0
	for i,j in zip(cover_frames, stego_frames):
		mse += image_mse(i,j)
	mse = mse/frameCount
	print("MSE:", mse)
	psnr = 20*math.log10(255) - 10*math.log10(mse)
	print("PSNR:", psnr)

def image_mse(img, stego_img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	stego_img = cv2.cvtColor(stego_img, cv2.COLOR_BGR2GRAY)
	h,w = img.shape[0:2]
	mse = 0.0
	for i in range(h):
		for j in range(w):
			mse = mse+(img[i,j] - stego_img[i,j])**2
	mse = mse/(h*w)
	print("I:", mse)
	return mse

if __name__ == '__main__':
	main()