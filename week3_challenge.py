"""Higher or Lower game"""
import random
randint=random.randint(1,100)

while True:
    guess=-1
    try:
        guess=int(input("Enter your guess"))
    except:
        print("Guess a *number* please.")

    if(guess<randint):
        print("Too low, try again!")
    elif(guess>randint):
        print("Too high, try again!")
    else:
        print("That's correct! Good job!")
        break