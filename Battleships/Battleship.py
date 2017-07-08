# coding=UTF-8
'''
Game features to add:

Make multiple battleships: 
you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. 
You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
DONE


Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or 
horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

TODO

fix rows <-> cols
legg til numrering på boardet

'''


from random import randint

board = []
ships = []

def conv_to_str(x):
	output = " "
	if x >= 10 and x < 100:
		output = str(x)
	elif x < 10:
		output = " "+str(x)
	else:
		output = "ERROR"
	return output
def create_board(x, y):
	for i in range(y):
		board.append(["O"] * x)

def print_board(board):
	nList = []
	z = 0
	while z < len(board[0]):
		nList.append(conv_to_str(z))
		z += 1
	print " ", " ".join(nList)	
	i = 0
	for x in board:
		print conv_to_str(i), "  ".join(x)
		i += 1

def make_ship(board):
	x = randint(0, len(board[0]) - 1)
	y = randint(0, len(board) - 1)
	
	i = 0
	while i < len(ships):
		while (y == ships[i]["y"]) and (x == ships[i]["x"]):
			
			print "-------------------------"
			print len(ships), "Duplicate detected!"
			print "N-> X Y D"
			print str(len(ships))+"->", x, y, i
			print "-------------------------"
			i = 0
			x = randint(0, len(board[0]) - 1)
			y = randint(0, len(board) - 1)
			break
		i += 1	
	else:
		print str(len(ships))+"->", x, y, "OK"
	ship = {"x" : x, "y" : y, "z" : 0}
	return ship

#  User input start	
tempX = int(raw_input("How many rows do you want?(0-99) - "))
tempY = int(raw_input("How many columns do you want?(0-99) - "))
if tempX >= 100:
	tempX = 99
	print "X is too large, set to 99!"
if tempY >= 100:
	tempY = 99
	print "Y is too large, set to 99!"
create_board(tempX, tempY)


	
enemies = int(raw_input("How many ships do you want?(0-%d) - " % ((len(board)*len(board[0])))))		
if enemies > (len(board)*len(board[0])):
	print "Too many enemies for the board"
	print "Enemies set to board max:", (len(board)*len(board[0]))
	enemies = (len(board)*len(board[0]))

print "-------------------------"
print "N-> X Y" #debug
for i in range(enemies):
	newShip = make_ship(board)
	ships.append(newShip)

print "-------------------------"	
print "N-> X Y" #debug
for i in range(len(ships)):
	print str(i)+"->", ships[i]["x"], ships[i]["y"]	

print "-------------------------"	
print "SORTING"
ships = sorted(ships, key=lambda k: k['y'])
ships = sorted(ships, key=lambda k: k['x'])
print "N-> X Y" #debug
for i in range(len(ships)):
	print str(i)+"->", ships[i]["x"], ships[i]["y"]
	
print "-------------------------"
print "-------------------------"
print "-------------------------"
print "-------------------------"	
turns = enemies + 5
print "Let's play Battleship!"
print "You have", turns, "turns to take out all the ships"
print "-------------------------"
print "       "
print_board(board)
	
for turn in range(turns):
	print "           "
	print "Turn", turn + 1
	print "Turns left:", turns
	turns -= 1
	sunkenShips = 0
	
	guess_X = int(raw_input("Guess X:"))
	guess_Y = int(raw_input("Guess Y:"))
	
	if (guess_X < 0 or guess_X > len(board[0])) or (guess_Y < 0 or guess_Y > len(board)):
		print "Oops, that's not even in the ocean."
		
	elif(board[guess_Y][guess_X] == "X"):
		print "You guessed that one already."
		
	else:
		for i in range(len(ships)):
			if guess_X == ships[i]["x"] and guess_Y == ships[i]["y"]:
				sunkenShips = 1
				board[guess_Y][guess_X] = "X"
				ships[i]["z"] = 1
				
			elif not (guess_X < 0 or guess_X > len(board[0])) or (guess_Y < 0 or guess_Y > len(board)):
				board[guess_Y][guess_X] = "X"
					
		if sunkenShips == 1:
			print "You sunk my battleship!"
		else:
			print "You missed my battleship!"
			
		for i in reversed(range(len(ships))):
			if ships[i]["z"] == 1:
				ships.pop(i)
				
		if len(ships) == 0:
			print "You sunk all my ships!"
			print "Well played!"
			break
	
	print "-------------------------"
	print "          "
	print_board(board)
	if turns == 0:
		print "          "
		print "You are out of moves!"
		print "Game Over"
		break
		
		
		
