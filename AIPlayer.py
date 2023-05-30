
import random  
from Player import *

class AIPlayer(Player):
    
    def __init__(self, checker ,name, tiebreak, lookahead):
        """
            Constructs a new AI Player object by initializing an attribute 
            checker, num_moves, tiebreak and lookahead.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker,name)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """
            returns a string representing an AIPlayer object. 
        """
        s = self.name  + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
        return s
    
    def max_score_column(self,scores):
        """
            takes a list scores containing a score for each column on the board,
            and returns the index of the column with the maximum score. If one 
            or more are tied for the maximum score, the method should apply the 
            called AIPlayer's tiebreaking strategy.
        """
        maximum = max(scores)
        max_indices = []
        for i in range(len(scores)):
            if scores[i] == maximum:
                max_indices += [i]
        
        if self.tiebreak == 'LEFT':
            return min(max_indices)
        elif self.tiebreak == 'RIGHT':
            return max(max_indices)
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_indices)
        

    def scores_for(self,b):
        """
            takes a Board object b and determines the called AIPlayer‘s scores 
            for the columns in b.
        """
        scores= [50]*b.width
        
        for column in range(b.width):
            
            if b.can_add_to(column) == False:
                scores[column] = -1
                
            elif b.is_win_for(self.checker) == True:
                scores[column] = 100
                
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[column]= 0
                
            elif self.lookahead == 0:
                scores[column] = 50
                
            else:
                b.add_checker(self.checker,column)
                opp = AIPlayer(self.opponent_checker(),self.name,self.tiebreak, (self.lookahead -1))
                opp_scores = opp.scores_for(b)
                    
                if max(opp_scores) == 100:
                    scores[column] = 0
                if max(opp_scores) == 0:
                    scores[column] = 100
                if max(opp_scores) == 50:
                    scores[column] = 50
                        
                b.remove_checker(column)
            
                   
        return scores
    
    def next_move(self,b):
        """
            overrides (i.e., replaces) the next_move method that is inherited from Player. Rather 
            than asking the user for the next move, this version of next_move should return the 
            called AIPlayer‘s judgment of its best possible move. 
        """
        self.num_moves += 1
        move = self.max_score_column(self.scores_for(b))
        return move

     
