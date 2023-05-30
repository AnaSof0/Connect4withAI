
from Board import Board

class Player: 
 
    def __init__(self,checker,name):
        """
            Constructs a new Player object by initializing an attribute
            checker and an attribute num_moves
        """
        self.checker = checker
        self.num_moves = 0
        self.name=name
     
    def __repr__(self):
        """
            returns a string representing a Player object.
        """
        s =  self.name
        
        return s
    
    def opponent_checker(self):
        """
            returns a one-character string representing the checker of 
            the Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self,b):
        """
            accepts a Board object b as a parameter and returns the column
            where the player wants to make the next move.
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if col < 0 or col > (b.width -1):
                print ('Try again!')
            else:
                return col
