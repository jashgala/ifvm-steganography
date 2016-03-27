from Tkinter import *
import tkMessageBox
import cv2
import os
import ifvm_helper as ifvm
#
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
import media_embedder as embd


global remCap
global occ
occ=[]
global cover



class App(object):
    def __init__(self):        
        ## window configuration
        self.root = Tk()
        self.root.wm_title("STEGANOGRAPHY")
        self.root.geometry("500x700+500+0")
        ##
        self.L1 = Label (self.root, text= "Enter the Cover Video : ")
        self.L1.pack()
        ##
        self.E1 = StringVar()
        Entry(self.root, textvariable=self.E1).pack()
        ## Output what is input via E1
        self.BT = StringVar()
        self.BT.set("Done")
        Button(self.root, textvariable=self.BT, command=self.clicked).pack()
        self.root.mainloop()


    def clicked(self):
        global remCap  # need to write as global variable is defined in this function Later
        global cover
        cover= self.E1.get()
        cap = cv2.VideoCapture(cover)
        frameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.LO1 = Label (self.root, text="No. of frames : "+ str(frameCount))
        self.LO1.pack()
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames = ifvm.getAllFrames(cap)
        #print frames
        # define capacity of each data frame
        h, w = frames[0].shape[:2]
        pixelCount = h * w - 1
        
        self.LO2 = Label (self.root, text="No. of pixels per frame : "+ str(pixelCount))
        self.LO2.pack()
        TotalPixelCount=pixelCount*frameCount

        self.LO3 = Label (self.root, text="Total No. of pixels : "+ str(TotalPixelCount))
        self.LO3.pack()
        
        remCap=(3*TotalPixelCount)/8
        self.LO4 = Label (self.root, text="Total Pixel Count which u can embed : "+ str(remCap))
        self.LO4.pack()
        self.clicked2()

    def clicked2(self):
        stop =0
        #while  (stop==0 and remCap>0) :
        self.LO5 = Label (self.root, text="Enter the file name of the media you want to embed in the video: ")
        self.LO5.pack()
                
        self.E2 = StringVar()
        Entry(self.root, textvariable=self.E2).pack()
        
        self.BT = StringVar()
        self.BT.set("Display Info for further actions : ")
        Button(self.root, textvariable=self.BT, command=self.clicked3).pack()

    def clicked3(self):
        global remCap
        global cover
        global occ
        
        secret = self.E2.get()
        statinfo = os.path.getsize(secret)
        self.LO6= Label (self.root, text="Size of file: "+str(statinfo))
        self.LO6.pack()
        cover, occ = embd.embed(cover, secret, occ, saveLocation = "output.avi")

        self.LO13= Label (self.root, text="KEY : "+ embd.key) 
        self.LO13.pack()


        remCap=remCap-statinfo
        if remCap>0:
            self.LO7= Label (self.root, text="You can still embed : "+ str(remCap))
            self.LO7.pack()
            self.LO8= Label (self.root, text="Do u want to embed file : ")
            self.LO8.pack()
            self.LO9= Label (self.root, text="1: YES ")
            self.LO9.pack()
            self.LO10= Label (self.root, text="2: NO ")
            self.LO10.pack()
            
            self.E3 = StringVar()
            Entry(self.root, textvariable=self.E3).pack()
            
            self.BT2 = StringVar()
            self.BT2.set("Click TO Continue")
            Button(self.root, textvariable=self.BT2, command=self.clicked4).pack()
        else:
            self.LO11= Label (self.root, text="You cannot steganogarph files further")
            self.LO11.pack()

    def clicked4(self):
        ch = self.E3.get()
        if int(ch)==1:
            self.clicked2()
        else:
            self.LO12= Label (self.root, text="GOOD BYE")
            self.LO12.pack()


            
App()