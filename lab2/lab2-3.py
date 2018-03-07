def main():
    import random
    answer=random.randint(1,20)
    guessTime=0
    while guessTime<6:
        userGuess=int(input("Enter a guess (1-20): "))
        if userGuess >20:
            print("That number is not between 1 and 20!")
        elif userGuess <0:
            print("That number is not between 1 and 20!")
        elif userGuess==answer:
            print("Correct! The number was",answer)
            return
        else:
            if userGuess<answer:
                print("Too low")
            else:
                print("Too high")
            guessTime=guessTime+1
    print("You are out of guesses. The number was",answer)
main()
            