import serial
import os, time
from Colors import *
from ColorMatrix import ColorMatrix
from PIL import Image

SERIAL = serial.Serial("COM12", 230400, timeout= None)
print(SERIAL.readline())

def rainbow():
    MATRIX = ColorMatrix()
    while(True):
        for x in range(12):
            for y in range(12):
                MATRIX.setPixel(x,y, RED)
                print("test")
                MATRIX.printSerial(SERIAL)
                print((x,y))
        for x in range(12):
            for y in range(12):
                MATRIX.setPixel(x,y, BLUE)
                MATRIX.printSerial(SERIAL)
                print((x,y))
        for x in range(12):
            for y in range(12):
                MATRIX.setPixel(x,y, GREEN)
                MATRIX.printSerial(SERIAL)
                print((x,y))

def testimage():
    MATRIX = ColorMatrix.makeFromPng(".\\Images\\Testimg.png")
    MATRIX.printSerial(SERIAL)

def animation():
    x = 0
    MATRIX = ColorMatrix()
    while(True):
        frame = x%19 +1
        MATRIX = ColorMatrix.makeFromPng(f".\\Animation\\F{frame}.png", 1)
        MATRIX.printSerial(SERIAL)
        print(x)
        x+= 1

def gallery(directory):
    while(True):
        for file in os.listdir(directory):
            MATRIX = ColorMatrix.makeFromPng(directory + file, 1)
            MATRIX.printSerial(SERIAL)
            time.sleep(3)

            # MATRIX = ColorMatrix()
            # MATRIX.printSerial(SERIAL)

def playGif(path, frameskip = 1):
    img = Image.open(path)
    for framenr in range(0, img.n_frames,frameskip):
        img.seek(framenr)
        MATRIX = ColorMatrix.makeFromPIL(img, 1)
        MATRIX.printSerial(SERIAL)
