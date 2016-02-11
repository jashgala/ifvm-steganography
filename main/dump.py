# This file has been made only for testing purposes
from PIL import Image
import sys
import os
import base64

def main():
	cover = sys.argv[1]
	# cover = Image.open(cover)
	# secret = sys.argv[2]
	# secret = Image.open(secret)
	with open(cover, "rb") as imageFile:
		str = base64.b64encode(imageFile.read())
	with open("medOp.txt","w") as txt:
		txt.write(str)
	with open("outfile.txt","rb") as res:
		str = base64.b64decode(res.read())
	fh = open("imageToSave.jpg", "wb")
	fh.write(str)
	fh.close()


def encode(cover, secret):
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p = data.getpixel(x,y)


if __name__ == '__main__':
	main()
