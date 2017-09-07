import Global

''' Create walls on the board '''


class Walls(object):
    def __init__(self):
        w = len(Global.arr[0])
        h = len(Global.arr)
        for x in range(h):
            for y in range(w):
                if (y - 2) % 8 > 3:
                    Global.arr[x][y] = 'X'
                else:
                    Global.arr[x][y] = ' '
                if x % 4 > 1:
                    Global.arr[x][y] = ' '
                if (x < 2 or x > h - 3):
                    Global.arr[x][y] = 'X'
                if (y < 2 or y > w - 3):
                    Global.arr[x][y] = 'X'
                if Global.arr[x][y] == '@':
                    Global.arr[x][y] = ' '

    def __repr__():
        pass
