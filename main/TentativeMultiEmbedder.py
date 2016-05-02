from __future__ import print_function
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
import subprocess
import media_embedder as embd

def main():
	occ = []
	cover = raw_input("Enter the cover video for Steganography: ")
	original_cover = cover
	count = int(raw_input("Enter the number of files you want to steganograph to steganograph: "))
	for i in range(count):
		secret = raw_input("Enter the file name of the media you want to embed in the video: ")
		cover, occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")

	# print("Transcribing audio")
	# command = ["ffmpeg" , "-i" , original_cover , "-vn" , "-acodec" , "copy" , "output-audio.aac"]
	# subprocess.call(command)
	# command = ["ffmpeg" , "-i" , "output.avi" , "-i" , "output-audio.aac" , "-vcodec" , "copy" , "-acodec" , "copy" , "muxed_file.avi"]
	# subprocess.call(command)


def embed_multiple(cover, secret, occ, saveLocation):
	original_cover = cover
	for i in range(count):
		secret = raw_input("Enter the file name of the media you want to embed in the video: ")
		cover, occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")

if __name__ == '__main__':
	main()
	
