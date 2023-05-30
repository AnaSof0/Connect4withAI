
from Board import Board
from Player import Player
from AIPlayer import *
import random



def main_connect_4():
    print("Welcome to Connect 4")
    print()
    height = int(input("How many rows do you want to play with? (usually it is 6)"+'\n'))
    print()
    width=int(input("How many columns? (usually it is 7)"+'\n'))

    b= Board(height,width)
    print()
    
    choice = int(input("Would you like to play against a friend (1) or a computer? (2)"+'\n'))
    print()
    while(choice !=1 and choice !=2):
        choice = int(input("Would you like to play against a friend (1) or a computer? (2)"+'\n'))
        print()
    if (choice==1):
        friend_play(b)
    else:
        computer_type=int(input("Would you like to play with a random computer (3) , or an intelligent one? (4)"+'\n'))
        print()
        while (computer_type != 3 and computer_type !=4):
            computer_type=int(input("Would you like to play with a random computer (3) , or an intelligent one? (4)"+'\n'))
            print()
        if computer_type==3:
            random_play(b)
        else:
            AI_play(b)
            
                          
        
def friend_play(b):
    print()
    name1= input("Great, what's the name of player 1(X)?"+'\n')
    name2 = input("And what's the name for player 2? (O)"+'\n')
    p1 = Player("X",name1)
    p2 = Player("O",name2)
    play(p1,p2,b)

def random_play(b):
    print()
    name1= input("Great, what's your name player 1(X)?"+'\n')
    p1 = Player("X",name1)
    p2 = RandomPlayer("O", "Random")
    
    play(p1,p2,b)
    
def AI_play(b):
    print()
    name1= input("Great, what's your name player 1(X)?"+'\n')
    p1 = Player("X",name1)
    tiebreak = int(input("What tiebreak strategy do you want it to use? Left (1), Right (2), Random (0)"+'\n'))
    while(tiebreak!=1 and tiebreak !=2 and tiebreak !=0):
        tiebreak = int(input("What tiebreak strategy do you want it to use? Left (1), Right (2), Random (0)"+'\n'))
    if(tiebreak == 0):
        t= 'RANDOM'
    elif (tiebreak ==1):
        t='LEFT'
    else:
        t = 'RIGHT'
    print()
    lookahead = int(input("And lookahead plays? (The greater number you choose, the smarter the computer is)"+'\n'))
    while (lookahead<0):
        print("It has to be greater than or equal to 0...")
        lookahead = int(input("And lookahead plays? (The greater number you choose, the smarter the computer is)"+'\n'))
        
    p2 = AIPlayer("O", "AI", t,lookahead)
    
    
    
    play(p1,p2,b)
    
    

def play(p1,p2,b):
    print(b)
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
    
        
  
        
    
def process_move(p,b):
    """
        takes two parameters: a Player object p for the player whose move
        is being processed, and a Board object b for the board on which the
        game is being played.
        The function performs all of the steps involved in processing a 
        single move by player p on board b
    """
    
    print (str(p) + "'s turn")
    move = p.next_move(b)
    b.add_checker(p.checker,move)
    print()
    print (b)
    if b.is_win_for(p.checker)== True:
        print(str(p) + " wins in " + str(p.num_moves) + " moves.")
        print("Congratulations!")
        return True
    elif b.is_win_for(p.checker) == False and b.is_full() == True:
        print ("It's a tie!")
        return True
    else:
        return False




class RandomPlayer(Player):
    
    def next_move(self,b):
        """
            Overrides the next_move method inherited from Player. 
            Rather than asking for next move, it chooses a random 
            selected column.
        """
        
        available_c = []
        for c in range(b.width):
            if b.can_add_to(c) == True:
                available_c += [c]
                
        self.num_moves += 1
        col = random.choice(available_c)
        return col

            