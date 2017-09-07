import os
import sys
import Bomb
import time
import Board
import Getch
import Enemy
import Global
import Bomberman
from termcolor import colored

''' Basic structure definition of objects on my board '''
bombermanStruct = ['[', ']', '^']
bombStruct = ['1', '2', '3', '4', '5']
explosionStruct = ['@', '*']
enemyStruct = ['0']
brick = ['L']
powerset = ['$', '%', '&']

Init = [
    '_______ _______ ___ ___ ______  _______ _______ ___ ___ _______ _____ ',
    '|   _  \|   _   |   Y   |   _  \|   _   |   _   |   Y   |   _   |   _ \ ',
    '|.  1  /|.  |   |.      |.  1  /|.  1___|.  l   |.      |.  1   |.  |  |',
    '|.  _  \|.  |   |. \_/  |.  _  \|.  ____|.  _   |. \_/  |.  _   |.  |  |',
    '|:  1   |:  1   |:  |   |:  1   |:  1   |:  |   |:  |   |:  |   |:  |  |',
    '|::.. . |::.. . |::.|:. |::.. . |::.. . |::.|:. |::.|:. |::.|:. |::.|  |',
    '`-------`-------`--- ---`-------`-------`--- ---`--- ---`--- ---`--- --',
    '',
    'Press Enter to Continue',
    '© UTKARSH 2017'
]

Title = [
        ' ___  ___  __  __ ___ ___ ___ __  __   _   _  _ ',
        '| _ )/ _ \|  \/  | _ ) __| _ \  \/  | /_\ | \| |',
        '| _ \ (_) | |\/| | _ \ _||   / |\/| |/ _ \| .` |',
        '|___/\___/|_|  |_|___/___|_|_\_|  |_/_/ \_\_|\_|'
]

GameOver = [
            ' _____                        _____                ',
            '|  __ \                      |  _  |               ',
            '| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ ',
            '| | __ / _` | \'_ ` _ \ / _ \ | | | \ \ / / _ \ \'__|',
            '| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   ',
            ' \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   '
]

'''
    Initialization of Board, Bomberman,
    a global object that has its instance and Enemies
'''


getch = Getch._Getch()
Global.init()
board = Board.Board()
bomber = Bomberman.Bomber()
Global.bomberwoman = bomber

for i in range(Global.level+5):
    Global.enemies.append(Enemy.Enemy())
    Global.enemies[i].SetPosition(Global.enemyset[i][0], Global.enemyset[i][1])

''' Taking single character input using getch '''


def static_input():
    try:
        text = getch()
    except:
        text = None
    return text


''' Function to print player's faliure message when game gets over '''


def gamelost():
    line = os.get_terminal_size().lines
    col = os.get_terminal_size().columns
    for i in range(int((line-10)/2)):
        print()
    for i in GameOver:
        print(colored(i.center(col), "magenta", attrs=["bold"]))
    time.sleep(2)
    os.system('tput reset')
    sys.exit()


''' Construction and printing of board, bomberman, bombs and enemies '''


def construct_board():
    if bomber.GetLives() <= 0:
        Global.bombwoman = None
        time.sleep(2)
        os.system('tput reset')
        gamelost()

    os.system('tput reset')
    # Since output is colored, this is more efficient than 'clear'
    boardArray = Global.arr
    bomber.MakeBomber()
    for i in Global.bombs:
        i.MakeBomb()
    for i in Global.enemies:
        i.MakeEnemy()
    w = len(boardArray[0])
    h = len(boardArray)
    col = os.get_terminal_size().columns
    for i in Title:
        print(colored(i.center(80), "magenta", attrs=["bold"]))
    for x in range(h):
        for y in range(w):
            box = boardArray[x][y]
            if box in enemyStruct:
                print(colored(box, "red", attrs=["bold"]), end="")
            elif box in bombermanStruct:
                print(colored(box, "green", attrs=["bold"]), end="")
            elif box in powerset:
                print(colored(box, "magenta", attrs=["bold", "blink"]), end="")
            elif box in bombStruct:
                print(colored(box, "blue", attrs=["bold"]), end="")
            elif box in explosionStruct:
                print(colored(box, "magenta", attrs=["bold", "dark"]), end="")
            elif box in brick:
                print(colored(box, "yellow", attrs=["bold", "dark"]), end="")
            else:
                print(box, end='')
        print()
    print(colored("\nLevel:%s \t\t\t\t\t\t\t\t Lives:%s" %
                  (Global.level, bomber.GetLives()), "green", attrs=["bold"]))
    print(colored("Game Score:%s" % (Global.score), "green", attrs=["bold"]))

''' Function called when input is given to quit the game '''


def quit_game():
    sys.exit()
    print("Are you sure you want to quit? (yes/no)")
    try:
        choice = str(input())
    except KeyboardInterrupt:
        sys.exit()
    return choice

''' Function called to generate the next level for the game '''


def next_level():
    Global.enemyput = True
    Global.wallbuild = True
    getch = Getch._Getch()
    board = Board.Board()
    bomber.RemoveBomber()
    bomber.SetPosition(2, 2)
    bomber.MakeBomber()
    for i in range(Global.level+5):
        Global.enemies.append(Enemy.Enemy())
        Global.enemies[i].SetPosition(Global.enemyset[i][0],
                                      Global.enemyset[i][1])

''' Update and check deaths by bombs on the board '''


def bombs_update():
    for i in Global.bombs:
        i.checkTime(time.time())

''' Update and check deaths by/of enemies on the board '''


def enemy_update():
    if not len(Global.enemies):
        time.sleep(2)
        Global.level += 1
        ''' Removing this condition will make this game level infinite '''
        if Global.level > 5:
            os.system('tput reset')
            print("You won")
            sys.exit()
        os.system('tput reset')
        print("Level Cleared")
        time.sleep(1)
        print("Generating Next Level...")
        time.sleep(2)
        next_level()

    for i in Global.enemies:
        [x, y] = i.GetPosition()
        [p, q] = bomber.GetPosition()
        flag = 0
        if i.checkmurder(bomber):
            bomber.SetPosition(2, 2)
            bomber.MakeBomber()
        i.RemoveEnemy()
        etype = i.GetType()
        flag = True
        if etype == 2 or etype == 3:
            if i.move2():
                flag = False
        if etype == 1 or etype == 3:
            if i.move3():
                flag = False
        if flag:
            i.move1()
        i.MakeEnemy()
        if i.checkmurder(bomber):
            bomber.SetPosition(2, 2)
            bomber.MakeBomber()

''' Updatation of objects on the board '''


def movement():
    bombs_update()
    enemy_update()

while True:
    col = os.get_terminal_size().columns
    line = os.get_terminal_size().lines
    os.system('tput reset')

    for i in range(int((line-10)/2)):
        print()
    for i in Init:
        print(colored(i.center(col), "yellow", attrs=["bold"]))
    try:
        input()
    except:
        sys.exit()
    break

''' Main infinite loop of the board '''


while True:
    construct_board()
    try:
        mv = static_input()
        if not mv:
            movement()
            continue
    except KeyboardInterrupt:
        mv = 'q'

    if mv == 'q':
        choice = quit_game()
        if choice == 'yes':
            sys.exit()
        else:
            movement()
            continue
    elif mv == 'd':
        bomber.RemoveBomber()
        bomber.moveRight()
        bomber.MakeBomber()
    elif mv == 'a':
        bomber.RemoveBomber()
        bomber.moveLeft()
        bomber.MakeBomber()
    elif mv == 's':
        bomber.RemoveBomber()
        bomber.moveDown()
        bomber.MakeBomber()
    elif mv == 'w':
        bomber.RemoveBomber()
        bomber.moveUp()
        bomber.MakeBomber()
    elif mv == 'b':
        boom = Bomb.Bomb(bomber, time.time())
        '''
            This condition can be used to set interval between two bombs and
            thus number of bombs that could be present simutaneously on the
            board, to do so just check for len of Global.bombs array against
            required number of restricted bomb numbers.
        '''
        if boom.GetTime() - Global. lbombtime >= 1.5:
            Global.bombs.append(boom)
            Global.lbombtime = boom.GetTime()
            boom.MakeBomb()
        '''
        if not len(Global.bombs):
            Global.bombs.append(boom)
            Global.lbombtime = boom.GetTime()
            boom.MakeBomb()
        '''
    movement()
