import pygame
import random
import ColorMatrix
import Colors
import scripts

pygame.init()
done = False

COLORLIST = {0:Colors.BLACK, -1:Colors.GREEN, 1:Colors.RED}

screen = pygame.display.set_mode((100,100))


class Field:
    def __init__(self) -> None:
        self.matrix = [[0 for x in range(12)] for y in range(12)]
        self.snake = [(6,6)]
        self.matrix[6][6] = -1
        self.placeApple()

    def moveSnake(self, movement):
        global done
        nextTile = (self.snake[0][0]+movement[0], self.snake[0][1]+movement[1])
        print(nextTile)
        if nextTile[0] < 0 or nextTile[0] > 11 or nextTile[1] < 0 or nextTile[1] > 11:
            done = True
        elif self.matrix[nextTile[0]][nextTile[1]] == -1:
            done = True
        elif self.matrix[nextTile[0]][nextTile[1]] == 1:
            self.matrix[nextTile[0]][nextTile[1]] = -1
            self.snake.insert(0, (nextTile[0], nextTile[1]))
            self.placeApple()
        elif self.matrix[nextTile[0]][nextTile[1]] == 0:
            self.matrix[nextTile[0]][nextTile[1]] = -1
            self.snake.insert(0, (nextTile[0], nextTile[1]))
            self.matrix[self.snake[-1][0]][self.snake[-1][1]] = 0
            self.snake.pop(-1)

    def placeApple(self):
        placed = False
        while not placed:
            (x,y) = (random.randrange(0,12), random.randrange(0,12))
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 1
                placed = True

    def toColorMatrix(self):
        out = ColorMatrix.ColorMatrix()
        for x in range(12):
            for y in range(12):
                out.matrix[x][y] = COLORLIST[self.matrix[x][y]]
        return out


FIELD = Field()
movement = (0,-1)
while(not done):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement = (0,-1)
            if event.key == pygame.K_s:
                movement = (0,1)
            if event.key == pygame.K_a:
                movement = (-1,0)
            if event.key == pygame.K_d:
                movement = (1,0)
    FIELD.moveSnake(movement)
    MATRIX = FIELD.toColorMatrix()
    MATRIX.printSerial(scripts.SERIAL)
    


#done

MATRIX = ColorMatrix.ColorMatrix.makeFromPng(".\\Images\\ded.png", 1)
MATRIX.printSerial(scripts.SERIAL)

pygame.quit()


