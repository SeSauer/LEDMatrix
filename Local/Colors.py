
class Color:
    def __init__(self, r = 0, g = 0, b = 0) -> None:
        self.r = r
        self.g = g
        self.b = b
        

    def toByteString(self) -> bytearray:
        return bytearray([self.r, self.g, self.b])
    
    def writeToSerial(self, serial):
        toWrite = self.toByteString()
        serial.write(toWrite)
        serial.flush()

    def __str__(self) -> str:
        return f"({self.r},{self.g},{self.b})"
    

BLACK = Color(0,0,0)
WHITE = Color(255,255,255)
RED = Color(255, 0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)
PURPLE = Color(255,0,255)
YELLOW = Color(255, 255, 0)
CYAN = Color(0,255,255)
