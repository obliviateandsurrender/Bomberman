import Global


class Person(object):
    def __init__(self):
        self.shape = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.position = ['', '']
        self.lives = 1

    ''' Returns current lives of Person object '''
    def GetLives(self):
        return self.lives

    ''' Returns current position of Person object '''
    def GetPosition(self):
        return self.position

    ''' Sets position of Person object '''
    def SetPosition(self, x, y):
        self.position = [x, y]

    ''' Collect powerup function '''
    def powerfunction(self, powerup):
        if powerup == '$':
            self.lives += 1
        elif powerup == '%':
            Global.score += 500
        elif powerup == '&':
            for i in range(2):
                Global.enemies.remove(random.choice(Global.enemies))

    ''' Moves fucntionality for Person object '''
    def moveRight(self):
        [x, y] = self.GetPosition()
        powerset = ['$', '%', '&']
        static = ['1', '2', '3', '4', 'X', 'L', '@', '*']

        if Global.arr[x][y + 4] in static:
            pass
        else:
            if Global.arr[x][y+4] in powerset and self is Global.bomberwoman:
                self.powerfunction(Global.arr[x][y+4])
            self.SetPosition(x, y + 4)

    def moveLeft(self):
        [x, y] = self.GetPosition()
        powerset = ['$', '%', '&']
        static = ['1', '2', '3', '4', 'X', 'L', '@', '*']

        if Global.arr[x][y - 4] in static:
            pass
        else:
            if Global.arr[x][y-4] in powerset and self is Global.bomberwoman:
                self.powerfunction(Global.arr[x][y-4])
            self.SetPosition(x, y - 4)

    def moveUp(self):
        [x, y] = self.GetPosition()
        powerset = ['$', '%', '&']
        static = ['1', '2', '3', '4', 'X', 'L', '@', '*']

        if Global.arr[x-2][y] in static:
            pass
        else:
            if Global.arr[x-2][y] in powerset and self is Global.bomberwoman:
                self.powerfunction(Global.arr[x-2][y])
            self.SetPosition(x - 2, y)

    def moveDown(self):
        [x, y] = self.GetPosition()
        powerset = ['$', '%', '&']
        static = ['1', '2', '3', '4', 'X', 'L', '@', '*']

        if Global.arr[x+2][y] in static:
            pass
        else:
            if Global.arr[x+2][y] in powerset and self is Global.bomberwoman:
                self.powerfunction(Global.arr[x+2][y])
            self.SetPosition(x + 2, y)

    ''' Describing death of Person object '''
    def death(self):
        self.lives = self.lives - 1

    ''' Check if person object has died or not '''
    def checkdeath(self, bomb):
        [p, q] = bomb.GetPosition()
        [x, y] = self.GetPosition()
        if p == x and q != y:
            if abs(q-y) <= 4:
                self.death()
                return True
        if q == y and x != p:
            if abs(x-p) <= 2:
                self.death()
                return True
        if p == x and q == y:
            self.death()
            return True
        return False
