import random

def user():
    goal = random.randint(0,100)
    print(goal)
    guess = input("Your Guess:")
    time_left = 6
    print(goal)
    while  guess != "exit":
        if time_left >1:
            if int(guess) < goal:
                print("Too Low")
            elif int(guess) > goal:
                print("Too High")
            elif int(guess) == goal:
                print("Hooray you won!")
                break
            time_left -=1
            guess = input("Your Guess:")
        else:
            print("Ohh noyou lost, the correct number is ",goal)
            break

                
                                           
def computer():
    time_left = 6
    x=0
    y=100
    found=False
    while not found:
        goal = (x+y)//2
        print("Computer Guess:",goal)
        user_input = input("")
        if user_input == "win":
            print("Hooray the computer won")
            found=True
            break
        elif user_input == "exit":
            found=True
            break
        elif user_input == "+":
            x = goal+1
            time_left -=1
        elif user_input == "-":
            y = goal-1
            time_left -=1

def main():
    user_input1 = input("User or Computer:")
    while user_input1 != "User" and user_input1 != "Computer":
        user_input1 = input("User or Computer:")
        
    if user_input1 == "User":
        user()
    else:
        computer()

        
            
main()
    