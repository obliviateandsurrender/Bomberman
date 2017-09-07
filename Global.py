'''
Global objects that are used to store major states
in the game. These were used to prevent any circular
call issues or random function calls regarding imported
objects in the file.
'''


def init():
    global arr
    global lives
    global bombs
    global enemies
    global powerups
    global level
    global enemyset
    global wallbuild
    global brickset
    global score
    global enemyput
    global lbombtime
    global bomberwoman

    arr = [[' ' for x in range(80)] for y in range(42)]
    bombs = []
    enemies = []
    enemyput = True
    enemyset = []
    powerups = ['$', '%', '&']
    level = 1
    wallbuild = True
    brickset = []
    score = 0
    lbombtime = 0
