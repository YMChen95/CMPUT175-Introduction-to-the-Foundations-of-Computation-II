import random
# -----------------------------------------------------------------------------
# Battleship Game - Assignment 4 - CMPUT 175 - Winter 2015
# -----------------------------------------------------------------------------

class BattleshipGame:
    def __init__(self):
        self.computerShips = {"A":5,
                              "B":4,
                              "S":3,
                              "D":3,
                              "P":2}
        self.userShips = {"A":5,
                          "B":4,
                          "S":3,
                          "D":3,
                          "P":2}
        self.rounds = 0
        #setup blank 10x10 board
        self.userBoard=[[" " for i in range(10)] for j in range(10)]
        self.computerBoard=[[" " for i in range(10)] for j in range(10)]
# ---------------------------------------------------------------------------
    def incrementRounds(self):
        self.rounds += 1
# ---------------------------------------------------------------------------
    def getHits(self, computer):
        if computer:
            board = self.userBoard
        else:
            board = self.computerBoard
        hits = 0
        for i in range(10):
            for j in range(10):
                if board[i][j] == "#":
                    hits += 1
        return hits
# ---------------------------------------------------------------------------
    def getMisses(self, computer):
        if computer:
            board = self.userBoard
        else:
            board = self.computerBoard
        misses = 0
        for i in range(10):
            for j in range(10):
                if board[i][j] == "*":
                    misses += 1
        return misses
# ---------------------------------------------------------------------------       
    def drawBoards(self,hide):
        print ("    Computer's board:         User's board:         at round: %d" % self.rounds)
        print ("    1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10                   Computer Status:  User Status:")
        labels=['A','B','C','D','E','F','G','H','I','J']
        for i in range(10):
            print (" %c |" % (labels[i]), end="")   # Computer's board
        #print the board values, and cell dividers
            for j in range(10):
                if self.computerBoard[i][j] == "*" or self.computerBoard[i][j] == "#" or not hide:
                    print (self.computerBoard[i][j]+"|", end="")
                else: 
                    print (' |', end="")   
            print ("   %c |" % (labels[i]), end="") # User's board
        #print the board values, and cell dividers
            for j in range(10):
                print (self.userBoard[i][j]+"|", end="")
            if i == 0:
                print("  Nbr. of hits  :  %02d                %02d" % (self.getHits(True), self.getHits(False)), end="")
            elif i == 1:
                print("  Nbr. of misses:  %02d                %02d" % (self.getMisses(True), self.getMisses(False)), end="")
            elif i == 2:
                print("  Ships sunk    :  %02d                %02d" % (len(self.getEnemyFleet(False)[1]), len(self.getEnemyFleet(True)[1])), end="")
            else:
                k = i - 3
                if len(self.getEnemyFleet(False)[1]) > k:
                    computer_ship = whatShip(self.getEnemyFleet(False)[1][k]).ljust(18)
                else:
                    computer_ship = "".ljust(18)
                if len(self.getEnemyFleet(True)[1]) > k:
                    user_ship = whatShip(self.getEnemyFleet(True)[1][k]).ljust(18)
                else:
                    user_ship = "".ljust(18)
                print("                   %s%s" % (computer_ship, user_ship), end="")
            print ("")
# ---------------------------------------------------------------------------       
    def validatePlacement(self,computer,ship,size,x,y,ori):

        #validate the ship can be placed at the given coordinates
        # and places it if acceptable
        if ori == "v" and x+size > 10:
            return False
        elif ori == "h" and y+size > 10:
            return False
        else:
            if computer:
                board=self.computerBoard
            else:
                board=self.userBoard
            if ori == "v":
                for i in range(size):
                    if board[x+i][y] != " ":
                        return False
            elif ori == "h":
                for i in range(size):
                    if board[x][y+i] != " ":
                        return False
            # announce the ship to be placed
            if computer:
                print ("Computer placing a " + ship)
            else: 
                print ("You placed a " + ship)                
            #place the ship based on valid orientation and coordinates
            if ori == "v":
                for i in range(size):
                    board[x+i][y] = ship[0]
            else: # ori=="h"
                for i in range(size):
                    board[x][y+i] = ship[0]
        return True

# ---------------------------------------------------------------------------       
    def getEnemyFleet(self, computer):
        # returns a list of two lists. The first one has the sunken ships and the second the ships to sink
        if computer:
            fleet=self.userShips
        else:
            fleet=self.computerShips
        toSink=[]
        sunk=[]
        # check all ships in the armada of ennemy in the game instance        
        for ship in fleet.keys():
            if fleet[ship]==0:
                sunk.append(ship)
            else:
                toSink.append(ship)
        return [toSink,sunk]

# ---------------------------------------------------------------------------       
    def checkWinning(self, computer):
        # Check if there are still any pieces of ships left to hit on the board
        # board refers to either the board of the computer (if user is playing) or the user (if computer is playing)
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        # Loop to check all cells in the board
        # if any cell contains a char that is not empty, a miss or a hit return false        
        for i in range(10):
            for j in range(10):
                if board[i][j] != ' ' and board[i][j] != '*' and board[i][j] != '#':
                    return False
        return True

# ---------------------------------------------------------------------------       
    
    def makeA_Move(self, computer, x,y):
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        old=board[x][y]
        if old==" ":
            board[x][y]="*"
        elif old=="*" or old=="#":
            return old
        else:
            board[x][y]="#"
        return old
# ---------------------------------------------------------------------------       

    def checkIfSunk(self, computer,symbol):
        if computer:
            armada=self.userShips
        else:
            armada=self.computerShips
        
        # reduce size left of hit ship and check if sunk
        armada[symbol] -= 1
        if armada[symbol] == 0:
            return True
        return False
    
# ---------------------------------------------------------------------------       
def computerPlaceShips(game,ships):
    # Placing the computer ships in random positions
    for ship in ships.keys():
        #generate random coordinates and validate the postion
        valid = False
        while(not valid):
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            o = random.randint(0,1)
            if o == 0: 
                ori = "v"
            else:
                ori = "h"
            valid = game.validatePlacement(True,ship,ships[ship],x,y,ori)
    
# ---------------------------------------------------------------------------       
def userPlaceShips(game,ships):
    # Placing the user ships after asking the coordinates and the orientation of each
    # Coordinates are for the bow
    for ship in ships.keys():
        #get coordinates from user and vlidate the postion
        valid = False
        while(not valid):
            game.drawBoards(True)
            print ("Placing a", ship, "of size", ships[ship])
            # reading coordinates x y of new ship
            shipCoordinates=readCoordinates()
            x=shipCoordinates[0]
            y=shipCoordinates[1]
            # reading orientation of new ship
            validOrientation=False
            while not validOrientation:
                orientation=input("This ship is vertical or horizontal (v,h)? ").lower()
                if orientation == "v" or orientation == "h":
                    validOrientation=True                
            valid = game.validatePlacement(False,ship,ships[ship],x,y,orientation)
            if not valid:
                print ("Cannot place a", ship, "there. Stern is out of the board or collides with other ship.\nPlease take a look at the board and try again.")
                input("Hit ENTER to continue")

    game.drawBoards(False)         # DEBUGGING: Cheating to see where the computer ships are
    input("Done placing user ships. Hit ENTER to continue")

# ---------------------------------------------------------------------------       
def readCoordinates():
    # read coordinates x y on board from user and validate
    validCoordinates=False
    while not validCoordinates:
        cell=input("Enter coordinates x y (x in [A..J] and y in [1..10]):")
        cell=cell.split()
        if len(cell)==2:
            if cell[0].upper() in ['A','B','C','D','E','F','G','H','I','J'] and cell[1].isdigit():
                x=['A','B','C','D','E','F','G','H','I','J'].index(cell[0].upper())
                y=int(cell[1])-1
                if x>=0 and x<=9 and y>=0 and y<=9:
                    validCoordinates=True    
    return [x,y]
# ---------------------------------------------------------------------------       
def userMakesMove(game):
    # ask for coordinates for a move by user and try to make move
    # if move is a hit, check ship sunk and win condition 
    # return if user won    
    moveLigit=False
    while(not moveLigit):
        move=readCoordinates()
        x=move[0]
        y=move[1]
        beforeDropped = game.makeA_Move(False,x,y)
        #displaying current boards
        game.drawBoards(True)
        labels=['A','B','C','D','E','F','G','H','I','J']
        if beforeDropped=="*" or beforeDropped == "#":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " was already played. Try again.")
        elif beforeDropped == " ":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " is a miss.")
            moveLigit=True
        else:
            print ("Hit at " + labels[x] + " " + str(y+1))
            if game.checkIfSunk(False,beforeDropped): 
                print (whatShip(beforeDropped) + " sunk")
            moveLigit=True
#    input("Press RETURN to continue")        
    return game.checkWinning(False)        
        
# ----------------------------------------------------------------------
computerHit = False
hit_x = 0
hit_y = 0
prev_x = 0
prev_y = 0
direction = 0
def computerMakesMove(game):
    # generate coordinates for a move by computer and try to make move
    # if move is a hit, check ship sunk and win condition 
    # return if computer won
    global computerHit, hit_x, hit_y, prev_x, prev_y, direction
    moveLigit=False
    while(not moveLigit):
        if (not computerHit):
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
        else:
            if direction == 0:
                x = prev_x + 1
                y = prev_y
            elif direction == 1:
                x = prev_x
                y = prev_y + 1
            elif direction == 2:
                x = prev_x - 1
                y = prev_y
            elif direction == 3:
                x = prev_x
                y = prev_y - 1
                
            # end search
            if direction > 4:
                computerHit = False
                direction = 0
                continue
            
            # x, y out of bounds
            if x < 0 or x > 9 or y < 0 or y > 9:
                direction += 1
                continue
            
        beforeDropped = game.makeA_Move(True,x,y)
        #displaying current boards
        game.drawBoards(True)
        labels=['A','B','C','D','E','F','G','H','I','J']
        
        
        if beforeDropped=="*" or beforeDropped == "#":
            moveLigit=False
            
            # search a new direction
            if computerHit:
                prev_x = hit_x
                prev_y = hit_y
                direction += 1
                
        elif beforeDropped == " ":
            print ("Sorry computer, " + labels[x] + " " + str(y+1) + " is a miss.")
            moveLigit=True
            
            # search from the start x, y
            if computerHit:
                prev_x = hit_x
                prev_y = hit_y
                direction += 1
        else:    
            print ("Computer did a Hit at " + labels[x] + " " + str(y+1))
            
            # hit a ship
            if (not computerHit):
                computerHit = True
                hit_x = x
                hit_y = y
            
            # record the coordinates
            prev_x = x
            prev_y = y
            
            if game.checkIfSunk(True,beforeDropped):
                print (whatShip(beforeDropped) + " sunk")
                # start new search
                computerHit = False
                direction = 0
            moveLigit=True
            
    return game.checkWinning(True)

# ----------------------------------------------------------------------
def whatShip(symbol):
    # converting the symbol of a ship to the full name and returning it
    if symbol == "A":
        ship = "Aircraft Carrier"
    elif symbol == "B":
        ship = "Battleship"
    elif symbol == "S":
        ship = "Submarine" 
    elif symbol == "D":
        ship = "Destroyer"
    elif symbol == "P": 
        ship = "Patrol Boat"
    return ship    
    
# #############################################################################
def main():
    ships = {"Aircraft Carrier":5,
             "Battleship":4,
             "Submarine":3,
             "Destroyer":3,
             "Patrol Boat":2}    
    game=BattleshipGame()                   # create instance of the game
    computerPlaceShips(game,ships)          # Computer places its armada
    userPlaceShips(game,ships)              # User places the armada
    
    gameOver=False
    # game main loop
    while(not gameOver): 
       
        #user move
        winning=userMakesMove(game)

        #check if user won
        if winning:
            print ("Congratulations! User WON!")
            gameOver=True
        else:
            # display what remains of the fleet
            armada=game.getEnemyFleet(False)
            print ("Ships to sink:[", end="")
            for ship in armada[0]:
                print (whatShip(ship), " ", end="")
            print ("]  Ships sunk:[",end="")
            for ship in armada[1]:
                print (whatShip(ship), " ", end="")
            print("]")            
            game.incrementRounds()
            #computer move
            winning=computerMakesMove(game)
        
            #check if computer won
            if winning:
                print ("Sorry! Computer WON! Here is what the board looked like:")
                # display boards without hiding the computer ships
                game.drawBoards(False)
                input("Press ENTER to continue")
                gameOver=True
# ############################################################################# 
    
if __name__=="__main__":
    main()