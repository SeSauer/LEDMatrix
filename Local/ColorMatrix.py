from Colors import *
from PIL import Image
import time

class ColorMatrix:
    def __init__(self, size= 12, color = BLACK) -> None:
        self.size = size
        self.pixelcount = size * size
        self.matrix = [[color for x in range(size)]for y in range(size)]

    def setPixel(self, x,y,color):
        self.matrix[x][y] = color
    
    def numberToCoords(self, input:int):
        y = (input // self.size)
        if  y %2 ==0:
            x = input % self.size
        else:
            x = self.size - (input % self.size) - 1

        x = int(x)
        y = int(y)
        return (x,y)

    def printSerial(self, serial):
        print("pong")
        for x in range(self.size):
            for y in range(12):              #int(self.size / 2)
                coords = self.numberToCoords(x * (12) + y)
                self.matrix[coords[0]][coords[1]].writeToSerial(serial)
                #print("confirm")
            print(serial.readline())
        time.sleep(0.01)


    @classmethod
    def makeFromPng(cls, path = ".\\Images\\Testimg.png", mode = 0):
        with Image.open(path) as image:
            self = ColorMatrix.makeFromPIL(image, mode)
        return self

    @classmethod
    def makeFromPIL(cls, img, mode = 0):
        self = cls(12)
        image = img.convert("RGB")
        mode = Image.NEAREST if mode == 0 else Image.LANCZOS
        image = image.resize((self.size,self.size), resample=mode)
        for x in range(self.size):
            for y in range(self.size):
                r,g,b = image.getpixel((x,y))
                self.setPixel(x,y,Color(r,g,b))
        return self

    def __str__(self) -> str:
        out = ""
        for x in self.matrix:
            for y in x:
                out = out + y.__str__()
            out = out+"\n"
        return out#
    
    def show(self):
        image = Image.new("RGB", (self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                image.putpixel((x,y), self.matrix[x][y].asTuple())
        image.show()