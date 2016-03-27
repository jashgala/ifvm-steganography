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
import media_embedder as embd

def main():
	occ = []
	cover = raw_input("Enter the cover video for Steganography: ")
	count = int(raw_input("Enter the number of files you want to steganograph to steganograph: "))
	for i in range(count):
		secret = raw_input("Enter the file name of the media you want to embed in the video: ")
		cover, occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")

def embed_multiple(cover, secret, occ, saveLocation):
	for i in range(count):
		secret = raw_input("Enter the file name of the media you want to embed in the video: ")
		cover, occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")

# ffmpeg -i bunny.flv -vn -acodec copy output-audio.m4a
# ffmpeg -i output.avi -i output-audio.aac -vcodec copy -acodec copy muxed_file.avi
if __name__ == '__main__':
	main()
	
