import serial
from ColorMatrix import ColorMatrix
from Colors import * 


SERIAL = serial.Serial("/dev/ttyACM0", 230400, timeout= None)

MATRIX = ColorMatrix(12)

MATRIX.printSerial(SERIAL)
print(1)

MATRIX.setPixel(0,0,Color(255,0,0))
MATRIX.setPixel(0,1,Color(255,0,0)) 
MATRIX.printSerial(SERIAL)

print(2)