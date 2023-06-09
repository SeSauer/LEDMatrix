import serial
from Colors import *
from ColorMatrix import ColorMatrix

SERIAL = serial.Serial("COM12", 230400, timeout= None)


SIZE = 12
PIXELCOUNT = SIZE*SIZE


MATRIX = ColorMatrix.makeFromPng("C:\\Users\\selus\\Documents\\Programmiersachen\\LEDMatrix\\Testimg.png")
MATRIX.printSerial(SERIAL)