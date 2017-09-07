import Global
import random

''' Create bricks on the board '''


class Bricks(object):
    def __init__(self):
        if Global.wallbuild:
            w = len(Global.arr[0])
            h = len(Global.arr)
            ''' Find empty valid positions on board '''
            for x in range(4, h-2, 2):
                for y in range(6, w-2, 4):
                    if random.randint(0, 1) and random.randint(0, 1):
                        if Global.arr[x][y] == ' ':
                            Global.brickset.append([x, y])
            Global.wallbuild = False
            ''' Select some of these input as place for enemy spawn '''
            if Global.enemyput:
                for i in range(Global.level + 5):
                    eset = random.choice(Global.brickset)
                    Global.enemyset.append(eset)
                    Global.brickset.remove(eset)
                Global.enemyput = False

        for i in Global.brickset:
            for j in range(4):
                Global.arr[i[0]][j + i[1]] = 'L'
                Global.arr[i[0] + 1][j + i[1]] = 'L'
