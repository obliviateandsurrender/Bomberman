BOMBERMAN
=========

A command line semi-colorized ASCII BOMBERMAN game based on non pygame and ncurses implemenation.

The project is implemented in python3 (and thus python2 is not supposed to be used).
Source code of this project resides in the src directory.

## Running the game 
Before running the code run the following code in the terminal.
``` sudo -H pip3 install termcolor ```
Reason of using termcolor was that inbuilt functionality of providing colours on shell screen looks quite
ugly though much more customizable.
Now the game can be run by the following code in the terminal. 
``` python3 Main.py ```

## Classes
The game contains several classes each of which represents an object in the game. These are as follows:-
* Board - Class to implement the main playing area that is the board for the game along with Walls and Bricks.
* Wall - Class to implement walls for the game that are indestructible.
* Brick - Class to implement bricks which can be destroyed be the bombs planted by the bomberman.
* Person - Parent class for the non static objects present in the game.
* Player - Class to implement the bomberman which will be operated by the user.
* Enemy - Class to implement the blood eating monster of the game, which will move according to different algorithms provided.
* Bomb - Class to implement the bombs that will be planted by the bomberman.

#### Board
	It defines main playing area that is the board for the game.
	* Properties - walls, bricks
	* Methods - `__init__()`

#### Wall
	It defines the indestructible area of the board in the game
	* Properties - None
	* Methods - `__init__()`, `__repr__()`

#### Brick
	It defines the destructible types of wall which can be destroyed by bombs
	* Properties - None
	* Methods - `__init__()`, `__repr__()`

### Person
	Parent class for the moving objects which are enemies and the bomberman (player)
	* Properties - shape, position, lives
	* Methods - `__init__()`, `GetLives()`, `GetPosition()`, `powerfunction()`, `moveRight()`, `moveLeft()`, `moveDown()`, `moveUp()`

#### Bomberman
	It defines the main protagonist of the game i.e., Bomberman which is controlled by the user
	* Properties - shape, position, lives
	* Methods - `__init__()`, `__repr__()`,`MakeBomber()`, `RemoveBomber()`

#### Enemy
	It defines the enemies for the game which are made to move through an algorithm which makes their moves random in the starting levels and later on aggressive in the higher levels
	* Properties - position, type, lives, shape
	* Methods - `__init__()`, `GetType()`, `MakeEnemy()`, `RemoveEnemy()`, `checkmurder()`, `move1()`, `move2()`, `move3()`

#### Bomb
	It defines the bombs that will be planted by the bomberman
	* Properties - shape, time, exploded, give, position
	* Methods - `__init__()`, `GetPosition()`,`GetTime()`, `tick()`, `MakeBomb()`,`explosion()`, `explode()`, `checkTime()`


## Basic Controls
	* w - Up
	* s - Down
	* a - Left
	* d - Right
	* b - Place Bomb
	* q - Quit the game

## Symbols
	* [^^] - Bomberman
	   ][
	* XXXX - Wall
	  XXXX
	* LLLL - Bricks
	  LLLL
	* 0000 - Enemy > Type 1 (Random Walker)
	  0000
	* 0000 - Enemy > Type 2 (Bomb phobic)
	  0880
	* 0080 - Enemy > Type 3 (Semi-Boss 2 lives)
	  0880
	* 0880 - Enemy > Type 4 (Boss with 3 lives)
	  0880 
	* BOMB - Bomb
	  BOMB 
	* @@@@ - Explosion
	  @@@@
	* $$$$ - Powerup 1 > Extra Health
	  $$$$
	* %%%% - Powerup 2 > 500 points extra
	  %%%%
	* &&&& - Powerup 3 > Eliminate 2 random enemies
	  &&&&

## Features
1. Multilevel implementation. Though I have written code to manage it with infinite levels but have restricted on test to just 5 levels. Check comments in 'Main.py' to see the procedure.
2. Bomb with time ticker, explosion. Bomb counter is initially 3 seconds (could be changed). Multiple bombs are allowed but this could be easily changed and instructions to restrict this to a specific number is given in the 'Main.py'. As of now it is restricted by a second dealy. Bomb explosion is as specified in the rules.
3. 4 type of enemies which have different walking styles. New enemy appears on different levels in different proportions which are decided randomly. Enemy numbers are decided on the basis of the current level. Enemy 1 moves randomly, while 2 moves away from the bombs, 3 move towards enemy with double speed but also checks for bombs in the way and in the 4 has triple the speed and can do all type of intelligent moves and even have multiple lives.
4. Scoreboard. Brick breaking 20 points and enemy kill 100 points.
5. Lives for both Bomberman (3) and Boss (2), semiboss enemy (3).
6. Powerups implemented. Though not in accordance with the rules since it felt the idead given in rule favoured bomberman which I didn't want. Powerup will appear randomly behind a brick after explosion. 3 powerups provides extra life, 500 points and 2 enemy elimination feature.
7. Highly modular OOPS implementation which could be further furnished with extra time.
8. Splash Screens for Game Start and Game Over.
