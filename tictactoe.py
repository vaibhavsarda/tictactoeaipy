#a2ment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | a2.tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""


#name:akhil jarodia 2017130 B1
import random 
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0


# turn variable defines whose turn is now
turn = player1

def validmove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	import a2
	if move==1 and a2.tile1==0 :
		return True
	elif move==2 and a2.tile2==0 :
		return True	
	elif move==3 and a2.tile3==0 :
		return True	
	elif move==4 and a2.tile4==0 :
		return True
	elif move==5 and a2.tile5==0 :
		return True
	elif move==6 and a2.tile6==0 :
		return True
	elif move==7 and a2.tile7==0 :
		return True
	elif move==8 and a2.tile8==0 :
		return True
	elif move==9 and a2.tile9==0 :	
		return True
	else :
		return False						

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
		a2.tile1 |  tile2  | tile3
______|_________|______
a2.tile4 |  a2.tile5  | a2.tile6
______|_________|______
a2.tile7 |  a2.tile8  | tile9
______|_________|______
	"""
	import a2
	if a2.tile1==a2.tile4 and a2.tile4==a2.tile7 and a2.tile1!=0:
			return True
	elif a2.tile2==a2.tile5 and a2.tile5==a2.tile8 and a2.tile2!=0:
			return True
	elif a2.tile3==a2.tile6 and a2.tile9==a2.tile6 and a2.tile3!=0 :
			return True
	elif a2.tile1==a2.tile2 and a2.tile3==a2.tile2 and a2.tile1!=0:
			return True
			return True
	#elif a2.tile7==tile8 and a2.tile9==tile8 and a2.tile7!=0:
			#return True
	elif a2.tile7==a2.tile8 and a2.tile9==a2.tile8 and a2.tile7!=0:
		return True				
	elif a2.tile1==a2.tile5 and a2.tile9==a2.tile5 and a2.tile1!=0:
			return True				
	elif a2.tile3==a2.tile5 and a2.tile7==a2.tile5 and a2.tile3!=0:
			return True
	else :
			return False
			
				
	
def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	move=random.randint(1,9) 
	while validmove(move)==False:
		move=random.randint(1,9)
	return move	






def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	
	"""
	import a2
	if a2.tile1==a2.tile4 and a2.tile7==0:
			return 7
	elif a2.tile1==a2.tile7 and a2.tile4==0:
			return 4		
	elif a2.tile7==a2.tile4 and a2.tile1==0:
			return 1
	
	elif a2.tile2==a2.tile5 and a2.tile8==0:
			return 8
	elif a2.tile8==a2.tile5 and a2.tile2==0:
			return 2		
	elif a2.tile2==a2.tile8 and a2.tile5==0:
			return 5	

	elif a2.tile6==a2.tile9 and a2.tile3==0:
			return 3
	elif a2.tile3==a2.tile9 and a2.tile6==0:
			return 6		
	elif a2.tile3==a2.tile6 and a2.tile9==0:
			return 9						
	
	elif a2.tile1==a2.tile2 and a2.tile3==0:
			return 3
	elif a2.tile1==a2.tile3 and a2.tile2==0:
			return 2		
	elif a2.tile2==a2.tile3 and a2.tile1==0:
			return 1
	
	elif a2.tile4==a2.tile5 and a2.tile6==0:
			return 6
	elif a2.tile4==a2.tile6 and a2.tile5==0:
			return 5		
	elif a2.tile5==a2.tile6 and a2.tile4==0:
			return 4	

	elif a2.tile8==a2.tile9 and a2.tile7==0:
			return 7
	elif a2.tile9==a2.tile7 and a2.tile8==0:
			return 8		
	elif a2.tile7==a2.tile8 and a2.tile9==0:
			return 9	

	elif a2.tile3==a2.tile5 and a2.tile7==0:
			return 7
	elif a2.tile3==a2.tile7 and a2.tile5==0:
			return 5		
	elif a2.tile7==a2.tile5 and a2.tile3==0:
			return 3
	
	elif a2.tile1==a2.tile5 and a2.tile9==0:
			return 9
	elif a2.tile9==a2.tile1 and a2.tile5==0:
			return 5		
	elif a2.tile5==a2.tile9 and a2.tile1==0:
			return 1	

						

	
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	a=0;b=0
	import a2
	if a2.tile1==1:
		a+=1
	elif a2.tile1==2:
		b+=1
	if a2.tile2==1:
		a+=1
	elif a2.tile2==2:
		b+=1
	if a2.tile3==1:
		a+=1
	elif a2.tile3==2:
		b+=1				
	if a2.tile4==1:
		a+=1
	elif a2.tile4==2:
		b+=1
	if a2.tile5==1:
		a+=1
	elif a2.tile5==2:
		b+=1
	if a2.tile6==1:
		a+=1
	elif a2.tile6==2:
		b+=1
	if a2.tile7==1:
		a+=1
	elif a2.tile7==2:
		b+=1
	if a2.tile8==1:
		a+=1
	elif a2.tile8==2:
		b+=1
	if a2.tile9==1:
		a+=1
	elif a2.tile9==2:
		b+=1
	if a==b or a==b+1 :
		return True
	else :
		return False								

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	import a2
	flag=0
	if gametype==1:
		s1=0
		while win()==False and s1<9:
			s1+=1
			if a2.turn==a2.player1:
				x=takeNaiveMove()
				if x==1:
					a2.tile1=1
				if x==2:
					a2.tile2=1	
				if x==3:
					a2.tile3=1
				if x==4:
					a2.tile4=1	
				if x==5:
					a2.tile5=1
				if x==6:
					a2.tile6=1	
				if x==7:
					a2.tile7=1
				if x==8:
					a2.tile8=1	
				if x==9:
					a2.tile9=1
				a2.turn=a2.player2
				
				
			elif a2.turn==a2.player2:
				x=takeNaiveMove()
				if x==1:
					a2.tile1=2
				if x==2:
					a2.tile2=2	
				if x==3:
					a2.tile3=2
				if x==4:
					a2.tile4=2	
				if x==5:
					a2.tile5=2
				if x==6:
					a2.tile6=2	
				if x==7:
					a2.tile7=2
				if x==8:
					a2.tile8=2	
				if x==9:
					a2.tile9=2
				a2.turn=a2.player1		
				
					
	elif gametype==2:
		s2=0
		while win()==False and s2<9 :
			s2+=1
			if a2.turn==a2.player1:
				x=takeNaiveMove()
				if x==1:
					a2.tile1=1
				if x==2:
					a2.tile2=1	
				if x==3:
					a2.tile3=1
				if x==4:
					a2.tile4=1	
				if x==5:
					a2.tile5=1
				if x==6:
					a2.tile6=1	
				if x==7:
					a2.tile7=1
				if x==8:
					a2.tile8=1	
				if x==9:
					a2.tile9=1
				a2.turn=a2.player2
			elif turn==player2:
				x=takeStrategicMove()
				if x==1:
					a2.tile1=2
				if x==2:
					a2.tile2=2	
				if x==3:
					a2.tile3=2
				if x==4:
					a2.tile4=2	
				if x==5:
					a2.tile5=2
				if x==6:
					a2.tile6=2	
				if x==7:
					a2.tile7=2
				if x==8:
					a2.tile8=2	
				if x==9:
					a2.tile9=2
				a2.turn=a2.player1	
				
				
				
	elif gametype==3:
		s3=0
		while win()==False and s3<9:
			s3+=1
			if a2.turn==a2.player1:
				x=takeStrategicMove()
				if x==1:
					a2.tile1=1
				if x==2:
					a2.tile2=1	
				if x==3:
					a2.tile3=1
				if x==4:
					a2.tile4=1	
				if x==5:
					a2.tile5=1
				if x==6:
					a2.tile6=1	
				if x==7:
					a2.tile7=1
				if x==8:
					a2.tile8=1	
				if x==9:
					a2.tile9=1
				a2.turn=a2.player2
			elif a2.turn==a2.player2:
				x=takeStrategicMove()
				if x==1:
					a2.tile1=2
				if x==2:
					a2.tile2=2	
				if x==3:
					a2.tile3=2
				if x==4:
					a2.tile4=2	
				if x==5:
					a2.tile5=2
				if x==6:
					a2.tile6=2	
				if x==7:
					a2.tile7=2
				if x==8:
					a2.tile8=2	
				if x==9:
					a2.tile9=2
				a2.turn=a2.player1
				
	if a2.tile1==1 and a2.tile4==1 and a2.tile7==1 :
		return 1
	elif a2.tile2==1 and a2.tile5==1 and a2.tile8==1 :
		return 1
	elif a2.tile3==1 and a2.tile6==1 and a2.tile9==1 :
		return 1
	elif a2.tile1==1 and a2.tile2==1 and a2.tile3==1 :
		return 1
	elif a2.tile4==1 and a2.tile5==1 and a2.tile6==1 :
		return 1
	elif a2.tile7==1 and a2.tile8==1 and a2.tile9==1 :	
		return 1
	elif a2.tile1==1 and a2.tile5==1 and a2.tile9==1 :
		return 1				
	elif a2.tile3==1 and a2.tile5==1 and a2.tile7==1 :
		return 1		
	
	elif a2.tile1==2 and a2.tile4==2 and a2.tile7==2 :
		return 2
	elif a2.tile2==2 and a2.tile5==2 and a2.tile8==2 :
		return 2
	elif a2.tile3==2 and a2.tile6==2 and a2.tile9==2 :
		return 2
	elif a2.tile1==2 and a2.tile2==2 and a2.tile3==2 :
		return 2
	elif a2.tile4==2 and a2.tile5==2 and a2.tile6==2 :
		return 2
	elif a2.tile7==2 and a2.tile8==2 and a2.tile9==2:	
		return 2
	elif a2.tile1==2 and a2.tile5==2 and a2.tile9==2 :
		return 2				
	elif a2.tile3==2 and a2.tile5==2 and a2.tile7==2 :
		return 2
	
				
	
def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	import a2
	t=0
	for i in range(n):
		a2.tile1=0;a2.tile2=0;a2.tile3=0;a2.tile4=0;a2.tile5=0;a2.tile6=0;a2.tile7=0;a2.tile8=0;a2.tile9=0
		x=game(1)

		if x==1:
			t+=1
	return (float(t)/float(n))		


def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	import a2
	t=0
	for i in range(n):
		a2.tile1=0;a2.tile2=0;a2.tile3=0;a2.tile4=0;a2.tile5=0;a2.tile6=0;a2.tile7=0;a2.tile8=0;a2.tile9=0
		x=game(2)
		if x==1:
			t+=1
	return (float(t)/float(n))

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	import a2
	a2.tile1=0;a2.tile2=0;a2.tile3=0;a2.tile4=0;a2.tile5=0;a2.tile6=0;a2.tile7=0;a2.tile8=0;a2.tile9=0
	t=0
	for i in range(n):
		a2.tile1=0;a2.tile2=0;a2.tile3=0;a2.tile4=0;a2.tile5=0;a2.tile6=0;a2.tile7=0;a2.tile8=0;a2.tile9=0
		x=game(3)
		if x==1:
			t+=1
	return (float(t)/float(n))
	
