class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        print(self.board[7],"|",self.board[8],"|",self.board[9],"\t","7","|","8","|","9")
        print("-----------     -----------")
        print(self.board[4],"|",self.board[5],"|",self.board[6],"\t","4","|","5","|","6")
        print("-----------     -----------")
        print(self.board[1],"|",self.board[2],"|",self.board[3],"\t","1","|","2","|","3")

#write some code here

#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise
        if " "not in self.board:
            return True
        else:
            return False
#write some code here

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
    
#write some code here
        try:
            cell=int(cell)
        except:
            cell=cell
        if cell in [1,2,3,4,5,6,7,8,9] :
            if self.board[cell] ==" ":
                return False
            else:
                return True
        else:
            return True
            
        
#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
    # assigns the cell of the board to the character ch
#write some code here
        self.board[cell]=ch
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
        if self.board[1]==self.board[2]==self.board[3]==ch or self.board[4]==self.board[5]==self.board[6]==ch or self.board[7]==self.board[8]==self.board[9]==ch or self.board[1]==self.board[4]==self.board[7]==ch or self.board[2]==self.board[5]==self.board[8]==ch or self.board[3]==self.board[6]==self.board[9]==ch or self.board[1]==self.board[5]==self.board[9]==ch or self.board[3]==self.board[5]==self.board[7]==ch:
            return True



#while True:
myboard=TicTacToe()
for letter in ["x","o","x","o","x","o","x","o","x"]:
    number=input("it is turn for "+letter+", what is your move?")
    while myboard.cellIsEmpty(number) :
        number=input("Invild enter,it is turn for "+letter+", what is your move?")
    number=int(number)
    myboard.assignMove(number,letter)
    myboard.drawBoard()
    if myboard.isWinner(letter):
        print(myboard.whoWon(),"wins.Congrats!")
        break
    if myboard.boardFull():
        print("That is a tie")
    
        
    