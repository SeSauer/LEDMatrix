import serial
from Colors import *
from ColorMatrix import ColorMatrix

SERIAL = serial.Serial("COM12", 230400, timeout= None)


SIZE = 12
PIXELCOUNT = SIZE*SIZE


MATRIX = ColorMatrix(SIZE, BLUE)

for x in range(5):
    MATRIX.printSerial(SERIAL)
    print(x)


MATRIX.setPixel(5,5,GREEN)

MATRIX.printSerial(SERIAL)