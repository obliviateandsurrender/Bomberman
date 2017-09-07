import Global
'''
*** DISCLAIMER ***
PLEASE SEE.

In order to make single character input this module defintion was copied
as it is from internet with some minor tweaks in it for unbuffering and
hence continuous iteration of main game loop. Another reason to include
this as a separate file was its lack of compatibility at most debian systems
if installed using pip3, for example on my system running Mint 18.2 getch
module could not be installed using pip3 and hence this method was used as
an alternative for bettering the game code and removing further such
dependencies (of os).
'''
'''
Gets a single character from standard input.
Does not echo to the screen.
'''


class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

'''Fetch and character using the termios module.'''


class _GetchUnix:
    def __init__(self):
        import tty
        import sys
        from select import select

    def __call__(self):
        import sys
        import tty
        import termios
        from select import select

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        '''
            i shall evaluate to [] untill a input comes in the specified stream
            which is stdin (standard input) in our case.
        '''
        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select([sys.stdin.fileno()], [], [], 1 -
                               (Global.level/20))
            # Change speed with level. Thus speed of main loop increases.
            if i:
                ch = sys.stdin.read(1)
                # If a character comes return it immidiately
            else:
                ch = None
                '''
                    Else None is provided.
                    Thus continious input is being feeded to getch()
                    and hence while loop iterates continously.
                '''
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

'''Fetch a character using the Microsoft Visual C Runtime.'''


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        import time

        # Delay timeout to match UNIX behaviour
        time.sleep(1)

        # Check if there is a character waiting, otherwise this would block
        if msvcrt.kbhit():
            return msvcrt.getch()

        else:
            return

getch = _Getch()
