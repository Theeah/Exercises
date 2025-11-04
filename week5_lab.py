"""Fixing/reformatting pre-made code."""
#Exercise 1
def left_path_scene():
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")

def right_path_scene():
    print("You walk down the right path and encounter a sleeping bear.")
    choice2 = input("Do you 'tiptoe' past or 'run' away? ")
    if choice2 == 'tiptoe':
        print("You successfully sneak past the bear. You win!")
    elif choice2 == 'run':
        print("You trip while running and the bear wakes up. You lose.")
    else:
        print("Invalid choice. You are lost.")

def start_scene():
    print("You are in a dark forest. You see two paths.")
    choice1 = input("Do you go 'left' or 'right'? ")
    if choice1 == 'left':
        left_path_scene()
    elif choice1 == 'right':
        right_path_scene()
    else:
        print("Invalid choice. You are lost.")

start_scene()

#Exercise 2 and 3?
# BROKEN Code Block


def add_points():
    # Bug: This creates a new LOCAL variable
    player_score = 10
    print(f"[Inside Function] Score is now: {player_score}")
    return player_score
# --- Main Program ---
player_score=0
print(f"[Outside] Player score is: {player_score}")
player_score=add_points()
print(f"[Outside] Player score is: {player_score}")

#Exercise 4
"""CALCULATOR
START
Type of operation?
Add:
    INSERT num1 AND num2
    add num1 and num2
Minus:
    INSERT num1 AND num2
    take num2 from num1
Multiply:
    INSERT num1 AND num2
    times num1 and num2
Divide:
    INSERT num1 AND num2
    IF num2==0:
        OUTPUT "Error, dividing by 0."
    divide num1 by num2
END"""

#Exercise 5
"""Test Plan:
0C
100C
-100C"""

def cel_to_fahr(celsius):

    """Changes the hard-coded degrees in celsius to degrees in fahrenheit."""
    fahrenheit = (celsius*(9/5)) + 32 #Changes the degrees in celsius to degrees in fahrenheit.

    print(f"{celsius} degrees celsius is {fahrenheit} in fahrenheit.") #The print command outputs a statement to the terminal.
    return fahrenheit

"""The higher the degrees in celsius, the higher the degrees in fahrenheit.
1 degree higher in celsius is 1.8 degrees higher in fahrenheit."""
assert cel_to_fahr(0)==32.0
assert cel_to_fahr(100)==212.0