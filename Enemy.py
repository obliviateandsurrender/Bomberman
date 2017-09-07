import Global
import random
from Person import Person

''' Enemy class inheriting from Person '''


class Enemy(Person):
    def __init__(self):
        self.position = [7, 2]
        self.type = random.randint(0, Global.level-1)
        ''' Structure of Enemies '''
        if self.type < 1:
            self.shape = [['0', '0', '0', '0'], ['0', '0', '0', '0']]
            self.lives = 1
        elif self.type < 2:
            self.shape = [['0', '0', '0', '0'], ['0', '8', '8', '0']]
            self.lives = 1
        elif self.type < 3:
            self.shape = [['0', '0', '8', '0'], ['0', '8', '8', '0']]
            self.lives = 2
        else:
            self.shape = [['0', '8', '8', '0'], ['0', '8', '8', '0']]
            self.lives = 3

    ''' Return Type '''
    def GetType(self):
        return self.type

    ''' Make enemy on the board '''
    def MakeEnemy(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            Global.arr[x][i + y] = self.shape[0][i]
            Global.arr[x + 1][i + y] = self.shape[1][i]

    ''' Remove enemy from the board '''
    def RemoveEnemy(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            Global.arr[x][i + y] = ' '
            Global.arr[x + 1][i + y] = ' '

    ''' Check murder by the enemy '''
    def checkmurder(self, bomber):
        [p, q] = bomber.GetPosition()
        [x, y] = self.GetPosition()
        if p == x and q == y:
            bomber.death()
            return True
        else:
            return False

    ''' Types of move performed by different enemies '''
    def move1(self):
        move = random.randint(0, 3)
        if move == 0:
            self.moveDown()
        elif move == 1:
            self.moveLeft()
        elif move == 2:
            self.moveRight()
        else:
            self.moveUp()

    def move2(self):
        [x, y] = self.GetPosition()
        [p, q] = Global.bomberwoman.GetPosition()
        if x == p:
            if y - q < 6 and y - q > 0:
                self.moveLeft()
                self.moveLeft()
            if q - y < 6 and q - y > 0:
                self.moveRight()
                self.moveRight()
        if y == q:
            if x - p < 6 and x - p > 0:
                self.moveUp()
                self.moveUp()
            if p - x < 6 and p - x > 0:
                self.moveDown()
                self.moveDown()
        if [x, y] != self.GetPosition():
            return True
        else:
            return False

    def move3(self):
        [x, y] = self.GetPosition()
        bombStruct = ['1', '2', '3', '4', '*', '@']
        if Global.arr[x][y+4] in bombStruct:
            self.moveLeft()
            self.moveLeft()
        elif Global.arr[x][y-4] in bombStruct:
            self.moveRight()
            self.moveRight()
        elif Global.arr[x+2][y] in bombStruct:
            self.moveUp()
            self.moveUp()
        elif Global.arr[x-2][y] in bombStruct:
            self.moveDown()
            self.moveDown()
        if [x, y] != self.GetPosition():
            return True
        else:
            return False
