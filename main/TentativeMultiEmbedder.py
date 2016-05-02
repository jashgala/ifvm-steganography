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

occ = []
cover = raw_input("Enter the cover video for Steganography: ")
count = int(raw_input("Enter the number of files you want to steganograph to steganograph: "))
for i in range(count):
	secret = raw_input("Enter the file name of the media you want to embed in the video: ")
	occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")
