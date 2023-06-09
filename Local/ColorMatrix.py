from Colors import *
from PIL import Image

class ColorMatrix:
    def __init__(self, size:int, color = BLACK) -> None:
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

        return (x,y)

    def printSerial(self, serial):
        for x in range(self.pixelcount):
            coords = self.numberToCoords(x)
            self.matrix[coords[0]][coords[1]].writeToSerial(serial)
            (serial.readline())

    @classmethod
    def makeFromPng(cls, path):
        self = cls(12)
        with Image.open(path) as image:
            image = image.convert("RGB")
            image = image.resize((self.size,self.size), resample=Image.NEAREST)
            image.show()
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