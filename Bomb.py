import Global
import random


class Bomb(object):
    def __init__(self, bomber, time):
        self.shape = [['B', 'O', 'M', 'B'], ['B', 'O', 'M', 'B']]
        self.time = time
        self.position = bomber.GetPosition()
        self.exploded = False
        self.give = []

    ''' Make bomb on board '''
    def MakeBomb(self):
        [x, y] = self.GetPosition()
        for i in range(4):
            Global.arr[x][i + y] = self.shape[0][i]
            Global.arr[x + 1][i + y] = self.shape[1][i]

    ''' Returns current position of bomb '''
    def GetPosition(self):
        return self.position

    ''' Returns creation time of bomb '''
    def GetTime(self):
        return self.time

    ''' BONUS: Change bomb structure '''
    def tick(self, i):
        i = str(i)
        self.shape = [[i, i, i, i], [i, i, i, i]]

    ''' Defining explosion of bomb '''
    def explosion(self):
        [x, y] = self.GetPosition()
        self.exploded = True
        bomber = Global.bomberwoman

        if bomber.checkdeath(self):
            bomber.SetPosition(2, 2)
            bomber.MakeBomber()

        for j in Global.enemies:
            if j.checkdeath(self):
                if not j.GetLives():
                    Global.enemies.remove(j)
                    Global.score += 100

        for i in range(4):
            if Global.arr[x][y-4] == 'L':
                Global.brickset.remove([x, y-4])
                self.give = [x, y-4]
                Global.score += 20
            if Global.arr[x][y-4] != 'X':
                Global.arr[x][i + y - 4] = '@'
                Global.arr[x + 1][i + y - 4] = '@'

            if Global.arr[x][y+4] == 'L':
                Global.brickset.remove([x, y+4])
                self.give = [x, y+4]
                Global.score += 20
            if Global.arr[x][y+4] != 'X':
                Global.arr[x][i + y + 4] = '@'
                Global.arr[x + 1][i + y + 4] = '@'

            if Global.arr[x+2][y] == 'L':
                Global.brickset.remove([x+2, y])
                self.give = [x+2, y]
                Global.score += 20
            if Global.arr[x+2][y] != 'X':
                Global.arr[x+2][i + y] = '@'
                Global.arr[x + 1 + 2][i + y] = '@'

            if Global.arr[x-2][y] == 'L':
                Global.brickset.remove([x-2, y])
                self.give = [x-2, y]
                Global.score += 20
            if Global.arr[x-2][y] != 'X':
                Global.arr[x-2][i + y] = '@'
                Global.arr[x + 1 - 2][i + y] = '@'

    ''' Define after explosion effects of the bomb '''
    def explode(self):
        [x, y] = self.GetPosition()
        powerups = ['$', '%', '&']
        self.time = -1

        for j in Global.enemies:
            if j.checkdeath(self):
                if not j.GetLives():
                    Global.enemies.remove(j)
                    Global.score += 100

        for i in range(4):
            Global.arr[x][i + y] = ' '
            Global.arr[x + 1][i + y] = ' '

        for i in range(4):
            if Global.arr[x][y-4] != 'X':
                Global.arr[x][i + y - 4] = ' '
                Global.arr[x + 1][i + y - 4] = ' '

            if Global.arr[x][y+4] != 'X':
                Global.arr[x][i + y + 4] = ' '
                Global.arr[x + 1][i + y + 4] = ' '

            if Global.arr[x+2][y] != 'X':
                Global.arr[x+2][i + y] = ' '
                Global.arr[x + 1 + 2][i + y] = ' '

            if Global.arr[x-2][y] != 'X':
                Global.arr[x-2][i + y] = ' '
                Global.arr[x + 1 - 2][i + y] = ' '

    ''' Check if it's time for bomb to explode '''
    def checkTime(self, time):
        bomb_time = 3 - int(time) + int(self.time)
        if bomb_time >= 0:
            if bomb_time:
                self.tick(bomb_time)
            else:
                self.tick('*')
            if bomb_time < 0.5:
                self.explosion()
        elif bomb_time < 0:
            self.tick('*')
            if not self.exploded:
                self.explosion()
                return
            self.explode()
            if self.give and not random.randint(0, 25):
                powerup = random.choice(['$', '%', '&'])
                x = self.give[0]
                y = self.give[1]
                for i in range(4):
                    Global.arr[x][i + y] = powerup
                    Global.arr[x + 1][i + y] = powerup
            if bomb_time < -1.5:
                Global.bombs.remove(self)
