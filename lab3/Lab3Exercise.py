class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
       

#write some code here

#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise

#write some code here

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
       
#write some code here

#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
    # assigns the cell of the board to the character ch

#write some code here

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------   
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.

#write some code here
