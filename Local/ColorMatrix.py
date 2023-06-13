from Colors import *

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

    def clear(self):
        self.matrix = [[BLACK for x in range(self.size)]for y in range(self.size)]