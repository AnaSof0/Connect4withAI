
class Board:
    """ a data type for a Connect Four board
    """   
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
            
        for col in range(self.width-1):
            s += '---'
        s += '\n'
        
        number = 0
        for col in range(self.width):
            if number > 9:
                number = 0
                s += ' '+str(number)
                number += 1
            else:  
                s += ' '+str(number)
                number += 1
        return s

    def add_checker(self, checker, col):
        """ 
            adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O' col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    
    def reset(self):
        """
            resets the Board object on which it is called by setting all 
            slots to contain a space character.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
        
    
    def add_checkers(self, colnums):
        """ 
            takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self,col):
        """
            returns True if it is valid to place a checker in the column
            col on the calling Board object. Otherwise, returns False.
        """
        if col > (self.width -1) or col < 0:
            return False
        
        if self.slots[0][col] != ' ':
            return False
        else:
            return True
        
    
    def is_full(self):
        """
            returns True if the called Board object is completely full of
            checkers, and returns False otherwise.
        """
        full_c = 0
        for c in range(self.width):
            can_add = self.can_add_to(c)
            if can_add == False:
                full_c +=1
        if full_c == self.width:
            return True
        else:
            return False
        
    def remove_checker(self,col):
        """
            removes the top checker from column col of the called 
            Board object.
        """
        removed = 0
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                removed += 1
            else:
                row += 1
            if removed == 1:
                break
        
    def is_win_for(self,checker):
        """
            accepts a parameter checker that is either 'X' or 'O',
            and returns True if there are four consecutive slots 
            containing checker on the board. Otherwise, it should 
            return False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
            self.is_vertical_win(checker)== True or  \
            self.is_down_diagonal_win(checker) == True or \
            self.is_up_diagonal_win(checker) == True:
            return True
        
        return False
        
        
    def is_horizontal_win(self, checker):
        """ 
            Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                   return True

    # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self,checker):
        """
            Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
            
                if self.slots[row][col] == checker and \
                    self.slots[row +1][col] == checker and \
                    self.slots[row +2][col] == checker and \
                    self.slots[row +3][col] == checker:
                   return True
               
        return False
    
    def is_down_diagonal_win(self,checker):
        """
            Checks for diagonal win (for diagonals that go down
            from left to right) for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width-3):
            
                if self.slots[row][col] == checker and \
                    self.slots[row +1][col +1] == checker and \
                    self.slots[row +2][col+ 2] == checker and \
                    self.slots[row +3][col +3] == checker:
                   return True
               
        return False
        
    def is_up_diagonal_win(self,checker):
        """
            Checks for diagonal win (for diagonals that go up 
            from left to right) for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width-3):
            
                if self.slots[row +3][col] == checker and \
                    self.slots[row +2][col +1] == checker and \
                    self.slots[row +1][col+ 2] == checker and \
                    self.slots[row][col +3] == checker:
                   return True
                
        return False