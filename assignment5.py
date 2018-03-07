#name:Yipeng Zhou
#ID:1414119
#name:Mengyang Chen
#ID:1412408


#battleship
import random
class BattleshipGame:
    def __init__(self):
        self.userBoard=[]
        self.computerBoard=[]
        self.rounds=0
        #x,y are used to store the position the computer will hit in next step.
        self.x=1
        self.y=1
        #recordX and recordY are used to store the position the computer hunted
        self.recordX=0
        self.recordY=0
        #The length of the shortest user ship
        self.shortest=2
        #huntlist is the list of positions that the computer will hunt
        self.huntlist=[]
        
        #the variable 'phase' indicate the phase that the computer is in
        #1 indicates the computer will randomly shoot on the board
        #2 indicates the computer will hunt from the huntlist
        #3 indicates the computer will target  
        #4 indicates the computer has found the ship and is trying to destroy it
        self.phase=1
        
        #The direction that the computer hit in the previous move.
        #1 denotes right; 2 denotes down; 3 denotes left; 4 denotes up;
        #0 means that the computer didn't hit anything in previous step.
        self.shipDirection=0
        self.directions=[1,2,3,4]
        #computerMove indicates whether the computer has made a move
        self.computerMove=True

        
        for i in range(10):
            templist=[]
            for j in range(10):
                templist.append(" ")
            self.userBoard.append(templist)

        for i in range(10):
            templist=[]
            for j in range(10):
                templist.append(" ")
            self.computerBoard.append(templist)        
        #The two dictionaries indicate the ships that the user and the computer
        #still have. The number indicates the length left for each ship.
        self.userShips={'A':5,'B':4, 'S':3, 'D':3, 'P':2}
        self.computerShips={'A':5,'B':4, 'S':3, 'D':3, 'P':2}
    
    #function that counts the round after each times that user and computer have finish the hitting.   
    def incrementRounds(self):
        self.rounds=self.rounds+1
    
    #function that counts the number of missing after each times that user and computer have finish the hitting.    
    def getMisses(self,computer):
        misses=0  #initialized
        if computer:  #counts as computer missing
            for i in range(10):
                for j in range(10):
                    if self.userBoard[i][j]=='*': 
                        misses=misses+1
                        # counts that how many * computer board has and return the result as the miss times
            return misses
        else:
            for i in range(10):
                for j in range(10):
                    if self.computerBoard[i][j]=='*':
                        misses=misses+1 
                        # counts that how many * user board has and return the result as the miss times            
            return misses
    #function that counts the number of hitted after each times that user and computer have finish the hitting.    
    def getHits(self,computer):
        hits=0    #initialized
        if computer:    #counts as computer's correct hitting
            for i in range(10):
                for j in range(10):
                    if self.userBoard[i][j]=='#':
                        hits=hits+1
                        # counts that how many # computer board has 
                        #and return the result as the correct hitting times 
            return hits
        else:    #counts as user's correct hitting
            for i in range(10):
                for j in range(10):
                    if self.computerBoard[i][j]=='#':
                        hits=hits+1 
                        # counts that how many # user board has 
                        #and return the result as the correct hitting times 
            return hits
        
    # draw the game board function
    # it will not return the computer board if hide==True
    def drawBoard(self,hide):
        
        #two dictionaries indicates the horizontal axis and vertical axis
        lettertodigit={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
        digittoletter={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}
        
        #a dictionary that use five characters to represent those boats
        ships={'A':"Aircraft Carrier", 'B':"Battleship", 'S':"Submarine",'D':"Dystroyer", 'P':"Patrol Boat"}
        print("   Computer's board:         User's board           at round", self.rounds)
        #output the table(round)
        print("   1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10                   Computer Status:  User Status")
        
        userNotSunk, userSunk=self.getEnemyFleet(True)
        computerNotSunk, computerSunk=self.getEnemyFleet(False)
        maxSunkNum=max(len(userSunk),len(computerSunk))
        counter=0
        
        computerhits=self.getHits(True)#get computer's correct hitting
        userhits=self.getHits(False)#get user's correct hitting
        computermisses=self.getMisses(True)#get computer's missing
        usermisses=self.getMisses(False)#get computer's missing
        
        #creat the computer and user board
        for i in range(10):
            tempstr=digittoletter[i+1]+" "
            for j in range(10):
                if hide and self.computerBoard[i][j] in self.computerShips.keys():
                # if hide is true the ships will not display at computer board
                    tempstr=tempstr+'|'+' '
                else:
                # if hide is false the ships will display at computer board
                    tempstr=tempstr+'|'+self.computerBoard[i][j]
            tempstr=tempstr+'|   '+digittoletter[i+1]+' '

                    
            for j in range(10):
                tempstr=tempstr+'|'+self.userBoard[i][j]
            tempstr=tempstr+'|'
            if i==0:
                # creat the information table's first row
                # output the information about hitts number for both comuter and user
                tempstr=tempstr+"  Nbr. of hits  :  "
                if computerhits<10:
                    # if computer hits is less than 10, have to change it to double-digit
                    tempstr=tempstr+'0'+str(computerhits)
                else:
                    tempstr=tempstr+str(computerhits)
                
                tempstr=tempstr+"                "
                if userhits<10:
                    # if user hits is less than 10, have to change it to double-digit
                    tempstr=tempstr+'0'+str(userhits)
                else:
                    tempstr=tempstr+str(userhits)
            if i==1:
                # creat the information table's second row
                # output the information about misses number for both comuter and user                
                tempstr=tempstr+"  Nbr. of misses:  "
                if computermisses<10:
                    # if computer misses is less than 10, have to change it to double-digit
                    tempstr=tempstr+'0'+str(computermisses)
                else:
                    tempstr=tempstr+str(computermisses)
                
                tempstr=tempstr+"                "
                if usermisses<10:
                    # if user misses is less than 10, have to change it to double-digit
                    tempstr=tempstr+'0'+str(usermisses)
                else:
                    tempstr=tempstr+str(usermisses)
            if i==2:
                # creat the information table's third row
                # output the information about ships sunk number for both comuter and user                
                tempstr=tempstr+"  Ships sunk    :  0"+str(len(computerSunk))
                tempstr=tempstr+"                "
                tempstr=tempstr+'0'+str(len(userSunk))
            if i>2 and counter<maxSunkNum:
                stringname=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
                tempstr=tempstr+"                   "
                if counter<len(computerSunk):
                    tempname=list(ships[computerSunk[counter]])
                    stringname[0:len(tempname)]=tempname
                tempstr=tempstr+"".join(stringname)
                if counter<len(userSunk):
                    tempstr=tempstr+ships[userSunk[counter]]
                
                counter=counter+1

            print(tempstr)
            
    def validatePlacement(self,computer,ship,size,x,y,orientation):
        if x+size-1>10 and orientation=='H' or y+size-1>10 and orientation=='V':
        # check if the input is in the board range
        # if it is not return false
            return False
        else:
            if computer:# validate computer's placement
                if orientation=='H':# when computer wants to place the ship horizontally
                    for i in range (x-1,x+size-1):
                        if self.computerBoard[y-1][i]!=' ':
                            return False
                    
                    for i in range (x-1,x+size-1):
                        self.computerBoard[y-1][i]=ship
                        
                else:# when computer wants to place the ship vertically
                    for i in range (y-1,y+size-1):
                        if self.computerBoard[i][x-1]!=' ':
                            return False
                    for i in range (y-1,y+size-1):
                        self.computerBoard[i][x-1]=ship                        
                    
            else:# validate user's placement
                if orientation=='H':# when user wants to place the ship horizontally
                    for i in range (x-1,x+size-1):
                        if self.userBoard[y-1][i]!=' ':
                            return False
                        
                    for i in range (x-1,x+size-1):
                        self.userBoard[y-1][i]=ship
                        
                else:# when user want to place the ship vertically
                    for i in range (y-1,y+size-1):
                        if self.userBoard[i][x-1]!=' ':
                            return False
                    for i in range (y-1,y+size-1):
                        self.userBoard[i][x-1]=ship
        
        return True
    
                            
    def getEnemyFleet(self,computer):
        ships=['A','B','D','S','P']
        if computer:
            #return the sunk list for computer
            notSunk=self.userShips.keys()
            sunk=[]# a list used to record the computer's sunk ships
            for i in ships:
                if not i in notSunk:
                    sunk.append(i)
            
            return notSunk, sunk
        else:
            #return the sunk list for user
            notSunk=self.computerShips.keys()
            sunk=[]# a list used to record the user's sunk ships
            for i in ships:
                if not i in notSunk:
                    sunk.append(i)            
            return notSunk,sunk
      
    # function allows computer to calculate what is the smallest ship that user has
    # it will decide how the computer hunting strategy works
    def shortestUserShip(self):
        notSunk,temp=self.getEnemyFleet(True)
        #not sunk list for either computer or user
        if  'P' in notSunk:
            return 2
        # if Patrol Boat do not sink yet return the fleet as 2
        elif 'D' in notSunk or 'S' in notSunk:
            return 3
        # if Patrol Boat sunked but destroyer don't sink yet, return the fleet as 3
        elif 'B' in notSunk:
            return 4
        # if both Patrol Boat and destroyer sunked, but Battleship don't sink yet return the fleet as 4
        else:
            return 5
        # there is only one case that all the ships sunk except Aircraft Carrier
        # in this case, return the fleet as 5
    
    
    def buildHuntlist(self):
        step=self.shortestUserShip()
        #step is the fleet that we got at the above function
        for i in range(1,11):
            if i%step!=0:
                
                for j in range(i%step,11,step):
                    self.huntlist.append([i,j])
                
            else:
                for j in range(step,11,step):
                    self.huntlist.append([i,j])
        
    def checkWinning(self,computer):
        if computer:
            #check if computer has some ships left
            if len(self.userShips)>0:
                return False
            else:
                return True
            #return the wining of computer as true if no ships left in the list
        else:
            #check if computer has some ships left
            if len(self.computerShips)>0:
                return False
            else:
                return True
            #return the wining of computer as true if no ships left in the list
            
    def makeA_Move(self,computer,x,y):
        if computer:
            # in case of the computer is making a movement
            if self.userBoard[y-1][x-1]==' ':
                self.userBoard[y-1][x-1]='*'
                return ' '
            elif self.userBoard[y-1][x-1]=='*' or self.userBoard[y-1][x-1]=='#':
                return self.userBoard[y-1][x-1]
            else:
                temp=self.userBoard[y-1][x-1]
                self.userBoard[y-1][x-1]='#'
                return temp
        else:
            # in case of the user is making a movement
            if self.computerBoard[y-1][x-1]==' ':
                self.computerBoard[y-1][x-1]='*'
                return ' '
            elif self.computerBoard[y-1][x-1]=='*' or self.computerBoard[y-1][x-1]=='#':
                return self.computerBoard[y-1][x-1]
            else:
                temp=self.computerBoard[y-1][x-1]
                self.computerBoard[y-1][x-1]='#'
                return temp
            
    def checkIfSunk(self,computer,ship):
        if computer:
        # in case of the computer
            if self.userShips[ship]==0:
            #check if the length of that ship equal to zero
                #if yes, pop that ship from list
                # and return true
                self.userShips.pop(ship)
                return True
            else:
                return False
          
        else:
        # in case of the user
            if self.computerShips[ship]==0:
            #check if the length of that ship equal to zero
                #if yes, pop that ship from list
                # and return true
                self.computerShips.pop(ship)
                return True
            else:
                return False
            

# user place ships function
def userPlaceShips(game):
    ships=["Aircraft Carrier", "Battleship", "Submarine", "Dystroyer", "Patrol Boat"]
    sizechart={'A':5,'B':4,'S':3,'D':3,'P':2}
    
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    digits=[1,2,3,4,5,6,7,8,9,10]
    
    # a For loop allows user to place each size of ship every time
    for shipname in ships:
        print("Placing an ", shipname, "of size ", sizechart[shipname[0]])
        while True:
            coordinates=[]
            while True:
                coordinates=input("Enter coordinates x y (x in [A...J] and y in [1...10]): ").split()
                # handle the valide input
                if len(coordinates)!=2:
                    continue
                else:
                    if coordinates[0].upper() not in letters:
                        continue
                    elif float(coordinates[1]) not in digits:
                        continue
                    else:
                        break
                # Only if user enter the correct input, the program would continue
            while True:
                direction=input("This ship is vertical of horizontal (v,h)? ")
                # handle the valide input
                # Only if user enter the correct input, the program would continue
                if direction.upper()!='H' and direction.upper() !='V':
                    continue
                else:
                    break
            # if all the input information are correct, and that ship can be place at the board successfully
            # program would place the ships accoding to user's order
            if game.validatePlacement(False, shipname[0], sizechart[shipname[0]], int(coordinates[1]), letters.index(coordinates[0].upper()),direction.upper()):
                print("You placed a", shipname)
                game.drawBoard(True)
                break
            # any incorrect input would result a error feedback
            else:
                print("Cannot place a", shipname, "there. Stern is out of the board or collides with other ship.")
                print("Please take a look at the board and try again.")
                input("Hit ENTER to continue")
    input("Done placing user ships. Hit ENTER to continue")
    
# The user automatically places the ships
# This function is used to debug more quick
# Not neccessary for the assignment requirement
def userAutoShips(game):
    ships=["Aircraft Carrier", "Battleship", "Submarine", "Dystroyer", "Patrol Boat"]
    sizechart={'A':5,'B':4,'S':3,'D':3,'P':2}
    direction=['V','H']
    for shipname in ships:
        while True:
            x=random.randint(1,10)
            y=random.randint(1,10)
            temp=random.randint(0,1)
            if game.validatePlacement(False, shipname[0], sizechart[shipname[0]], x,y,direction[temp]):
                break
    #input("The user has finished placing ships! Hit ENTER to start to hit.")

#The computer places ships
def computerPlaceShips(game):
    ships=["Aircraft Carrier", "Battleship", "Submarine", "Dystroyer", "Patrol Boat"]
    sizechart={'A':5,'B':4,'S':3,'D':3,'P':2}
    direction=['V','H']
    for shipname in ships:
        while True:
            x=random.randint(1,10)#random chose the x axis postion from 1 to 10
            y=random.randint(1,10)#random chose the y axis postion from 1 to 10
            temp=random.randint(0,1)#random chose if place it vertical or horizontal
            if game.validatePlacement(True, shipname[0], sizechart[shipname[0]], x,y,direction[temp]):
                #check if it is a validated placement
                break
#The user making move function
def userMakeAMove(game):
    # 2 lists involve all the valid input information
    # it will be used to check if user's input is valid
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    ships={'A':"Aircraft Carrier", 'B':"Battleship", 'S':"Submarine",'D':"Dystroyer", 'P':"Patrol Boat"}
    digits=[1,2,3,4,5,6,7,8,9,10]    
    while True:
        while True:
            coordinates=input("Enter coordinates x y (x in [A..J] and y in [1..10]):").split()
            if len(coordinates)!=2:
                continue
            # check if the input value's length equals to 2
            # only if user enter the valid input the program would continue
            else:
                if coordinates[0].upper() not in letters:
                    # check if the input value on the letters' list
                    # only if user enter the valid input the program would continue
                    continue
                elif float(coordinates[1]) not in digits:
                    # check if the input value on the digits' list
                    # only if user enter the valid input the program would continue
                    continue
                else:
                    y=letters.index(coordinates[0].upper())
                    x=int(coordinates[1])
                    break    
            
        print("Hit at", coordinates[0].upper(), coordinates[1])
        move=game.makeA_Move(False, x, y)
        if move=='*' or move=='#':
            print("sorry", x, y, "already played. Try again")
            # check if the input value has been already placed
            # only if user enter the valid input the program would continue
            continue
        elif move==' ':
            break
        else:
            game.computerShips[move]=game.computerShips[move]-1
            if game.checkIfSunk(False,move):
                print(ships[move], "Sunk")
            break
    game.computerMove=False
    


#The computer making move function
def computerRandomMove(game):
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    digits=[1,2,3,4,5,6,7,8,9,10]    
    while True:
        x=random.randint(1,10)#random chose the x axis postion from 1 to 10
        y=random.randint(1,10)#random chose the y axis postion from 1 to 10
        move=game.makeA_Move(True, x,y)# when decide the postion, make a move in Class
        if move=='*' or move=='#':
            #if it has already been placed, continue
            continue
        elif move==' ':
            game.phase=2
            game.computerMove=True
            break
        else:
            game.userShips[move]=game.userShips[move]-1
            game.checkIfSunk(True,move)
            game.recordX=x
            game.recordY=y
            game.x=x
            game.y=y
            game.phase=3
            game.directions=[1,2,3,4]
            game.computerMove=True
            break
    print("Computer Hit at", letters[game.y], game.x)
    
def computerHunt(game):
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    digits=[1,2,3,4,5,6,7,8,9,10]    
    step=game.shortestUserShip()
    #find the smallest ship that still didn't sink 
    while True:
        position=random.choice(game.huntlist)
        game.x=position[1]
        game.y=position[0]
        game.huntlist.remove(position)
        move=game.makeA_Move(True, game.x, game.y)
        if move=='*':           
            continue
        elif move=='#':
            game.recordX=game.x
            game.recordY=game.y
            game.phase=3
            game.directions=[1,2,3,4]
            break
        elif move==' ':
            print("Computer Hit at", letters[game.y], game.x)
            game.computerMove=True
            break
        else:
            print("Computer Hit at", letters[game.y], game.x)
            game.userShips[move]=game.userShips[move]-1
            game.checkIfSunk(True,move)
            game.recordX=game.x
            game.recordY=game.y
            game.phase=3
            game.directions=[1,2,3,4]
            game.computerMove=True
            break    
    

def computerTarget(game):
    #randomly choose a direction to target the ship
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    digits=[1,2,3,4,5,6,7,8,9,10]    
    while True:
        #check if the length of the list of directions>0, if not, back to the hunting phase
        if len(game.directions)>0:
            
            direction=random.choice(game.directions)
        else:
            game.phase=1
            break
        if direction==1:
            #the position can not bigger than 10
            if game.recordX==10:
                game.directions.remove(direction)
                continue
            else:
                move=game.makeA_Move(True, game.recordX+1, game.recordY)
                #hunt the right of the original position
                #game.recordX=game.recordX+1
                if move=='*' or move=='#':
                    #remove the direction after the computer miss or hit
                    game.directions.remove(direction)
                    continue
                elif move==' ':
                    game.computerMove=True
                    game.directions.remove(direction)
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.recordY], game.recordX+1)
                    break
                else:
                    #computer make move if the position is available
                    print("Computer Hit at", letters[game.recordY], game.recordX+1)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)
                    #ship derecion, destroy phase
                    game.shipDirection=1
                    game.phase=4
                    game.computerMove=True
                    game.x=game.recordX+1
                    break
        if direction==2:
            #it is the same as in the direction1, but the direction changes
            if game.recordY==10:
                game.directions.remove(direction)
                continue
            else:
                move=game.makeA_Move(True, game.recordX, game.recordY+1)
                #hunt the right of the original position
                #game.recordX=game.recordY+1
                if move=='*' or move=='#':
                    game.directions.remove(direction)
                    continue
                elif move==' ':
                    game.computerMove=True
                    game.directions.remove(direction)
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.recordY+1], game.recordX)
                    break
                else:
                    print("Computer Hit at", letters[game.recordY+1], game.recordX)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move) 
                    #ship derecion, destroy phase
                    game.shipDirection=2
                    game.phase=4
                    game.computerMove=True
                    game.y=game.recordY+1
                    break
        if direction==3:
            if game.recordX==1:
                game.directions.remove(direction)
                continue
            else:
                move=game.makeA_Move(True, game.recordX-1, game.recordY)
                #hunt the right of the original position
                if move=='*' or move=='#':
                    game.directions.remove(direction)
                    continue
                elif move==' ':
                    game.computerMove=True
                    game.directions.remove(direction)
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.recordY], game.recordX-1)
                    break
                else:
                    print("Computer Hit at", letters[game.recordY], game.recordX-1)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)
                    #ship derecion, destroy phase
                    game.shipDirection=3
                    game.phase=4
                    game.computerMove=True
                    game.x=game.recordX-1
                    break
        if direction==4:
            if game.recordY==1:
                game.directions.remove(direction)
                continue
            else:
                move=game.makeA_Move(True, game.recordX, game.recordY-1)
                #hunt the right of the original position
                if move=='*' or move=='#':
                    game.directions.remove(direction)
                    continue
                elif move==' ':
                    game.computerMove=True
                    game.directions.remove(direction)
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.recordY-1], game.recordX)
                    break
                else:
                    print("Computer Hit at", letters[game.recordY-1], game.recordX)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)
                    #ship derecion, destroy phase
                    game.shipDirection=4
                    game.phase=4
                    game.computerMove=True
                    game.y=game.recordY-1
                    break

def computerDestroy(game):
    #computer destroy the whole ship that was targeted
    letters=[' ','A','B','C','D','E','F','G','H','I','J']
    digits=[1,2,3,4,5,6,7,8,9,10]     
    ships={'A':"Aircraft Carrier", 'B':"Battleship", 'S':"Submarine",'D':"Dystroyer", 'P':"Patrol Boat"}
    while True:
        #if the ship choose direction1 to target
        if game.shipDirection==1:
            #while the x value smaller than 10
            if game.x+1<11:
                game.x=game.x+1
                move=game.makeA_Move(True, game.x, game.y)
                #miss or hit
                if move=='*' or move=='#':
                    game.x=game.recordX #after the position is hit, x become recordx
                    game.directions.remove(game.shipDirection)
                    #randomly choose a direction
                    if len(game.directions)>0:
                        game.shipDirection=random.choice(game.directions)
                        continue
                    else:
                        #hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        break
                elif move==' ':
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.y], game.x)
                    game.x=game.recordX
                    game.computerMove=True
                    game.directions.remove(game.shipDirection)
                    #randomly choose a direction to hunt
                    if len(game.directions)>0:
                        game.shipDirection=random.choice(game.directions)
                    else:
                        #hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        
                    break
                else:
                    #game.x=game.x+1
                    #report the positon
                    print("Computer Hit at", letters[game.y], game.x)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)                      
                    game.computerMove=True
                    break

            else:
                #if the computer move to the position that has already been hit or missed
                game.x=game.recordX
                game.directions.remove(game.shipDirection)
                if len(game.directions)>0:
                    #randomly choose a direction to hunt
                    game.shipDirection=random.choice(game.directions)
                    continue
                else:
                    #back to hunting phase
                    game.directions=[1,2,3,4]
                    game.phase=1
                    break
        elif game.shipDirection==2:
            #while the y value smaller than 10
            if game.y+1<11:
                game.y=game.y+1
                move=game.makeA_Move(True, game.x, game.y)
                if move=='*' or move=='#':
                    game.y=game.recordY#after the position is hit, y become recordy
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                        #randomly choose a direction
                        game.shipDirection=random.choice(game.directions)
                        continue
                    else:
                        #back to hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        break
                elif move==' ':
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.y], game.x)
                    game.y=game.recordY
                    game.computerMove=True
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                        #randomly choose a direction to hunt
                        game.shipDirection=random.choice(game.directions)
                    else:
                        #back to the hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        
                    break
                else:
                    print("Computer Hit at", letters[game.y], game.x)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)                      
                    game.computerMove=True
                    break

            else:
                #if the computer move to the position that has already been hit or missed
                game.y=game.recordY
                game.directions.remove(game.shipDirection)
                if len(game.directions)>0:
                    #randomly choose a direction to hunt
                    game.shipDirection=random.choice(game.directions)
                    continue
                else:
                    #back to hunting phase
                    game.directions=[1,2,3,4]
                    game.phase=1
                    break
        elif game.shipDirection==4:
            #while the y value greater than 1
            if game.y-1>0:
                game.y=game.y-1
                move=game.makeA_Move(True, game.x, game.y)
                if move=='*' or move=='#':
                    game.y=game.recordY#after the position is hit, y become recordy
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                        #randomly choose a direction
                        game.shipDirection=random.choice(game.directions)
                        continue
                    else:
                        #back to the hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        break
                elif move==' ':
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.y], game.x)
                    game.y=game.recordY
                    game.computerMove=True
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                        #randomly choose a direction to hunt
                        game.shipDirection=random.choice(game.directions)
                    else:
                        #back to hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        
                    break
                else:
                    print("Computer Hit at", letters[game.y], game.x)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)                      
                    game.computerMove=True
                    break

            else:
                #if the computer move to the position that has already been hit or missed
                game.y=game.recordY
                game.directions.remove(game.shipDirection)
                if len(game.directions)>0:
                    #randomly choose a direction to hunt
                    game.shipDirection=random.choice(game.directions)
                    continue
                else:
                    #back to hunting phase
                    game.directions=[1,2,3,4]
                    game.phase=1
                    break
        elif game.shipDirection==3:
            #while the y value greater than 1
            if game.x-1>0:
                game.x=game.x-1
                move=game.makeA_Move(True, game.x, game.y)
                if move=='*' or move=='#':
                    game.x=game.recordX#after the position is hit, x become recordx
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                         #randomly choose a direction
                        game.shipDirection=random.choice(game.directions)
                        continue
                    else:
                        #back to hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        break
                elif move==' ':
                    #report the position that computer hits
                    print("Computer Hit at", letters[game.y], game.x)
                    game.x=game.recordX
                    game.computerMove=True
                    game.directions.remove(game.shipDirection)
                    if len(game.directions)>0:
                        #randomly choose a direction to hunt
                        game.shipDirection=random.choice(game.directions)
                    else:
                        #back to hunting phase
                        game.directions=[1,2,3,4]
                        game.phase=1
                        
                    break
                else:
                    print("Computer Hit at", letters[game.y], game.x)
                    game.userShips[move]=game.userShips[move]-1
                    #check if the ship is sunk
                    game.checkIfSunk(True,move)                      
                    game.computerMove=True
                    break

            else:
                #if the computer move to the position that has already been hit or missed
                game.x=game.recordX
                game.directions.remove(game.shipDirection)
                if len(game.directions)>0:
                    #randomly choose a direction to hunt
                    game.shipDirection=random.choice(game.directions)
                    continue
                else:
                    #back to hunting phase
                    game.directions=[1,2,3,4]
                    game.phase=1
                    break
    
def smartcomputerMakeAMove(game):
    #computer move according to different phases
    while True:
        #phase1:hunt randomly
        if game.phase==1:
            computerRandomMove(game)
            break
        #phase2:randomly choose a position to hunt in the hunt list
        elif game.phase==2:
            computerHunt(game)
            break
        #phase3:randomly choose a direction to target the hunted ship 
        elif game.phase==3:
            computerTarget(game)
            break
        #destroy the whole ship that was hunted
        else:
            computerDestroy(game)
            break
    
def main(): 
    mygame=BattleshipGame()
    #draw a board and hide the computer's ship
    mygame.drawBoard(True)
    #userAutoShips(mygame)
    userPlaceShips(mygame)
    computerPlaceShips(mygame)
    mygame.drawBoard(True)
    #creat a list of positions that are chosen by the shortest ship size for the further improvment
    mygame.buildHuntlist()
    while True:
        if mygame.computerMove==True:
            mygame.incrementRounds()#to count the rounds
            userMakeAMove(mygame)
            mygame.computerMove=False
            if mygame.checkWinning(False):
                break
        else:
            #computer move according to different phases
            smartcomputerMakeAMove(mygame)
            if mygame.checkWinning(True):
                break
            
        if mygame.computerMove:
            mygame.drawBoard(True)
            
    mygame.drawBoard(True)
    #give the result after either computer or user lose the game
    if len(mygame.userShips)==0:
        print("Too bad! The computer won!")
    else:
        print("Congratulations! User WON!")
        
        
main()


            