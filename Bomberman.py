import Global
from Person import Person


class Bomber(Person):
    def __init__(self):
        self.shape = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
        self.position = [2, 2]
        self.lives = 3

    ''' Make bomberman on board '''
    def MakeBomber(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            Global.arr[x][i + y] = self.shape[0][i]
            Global.arr[x + 1][i + y] = self.shape[1][i]

    ''' Remove bomberman on board '''
    def RemoveBomber(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            Global.arr[x][i + y] = ' '
            Global.arr[x+1][i + y] = ' '
