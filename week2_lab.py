#Exercise 1
"""Changes the hard-coded degrees in celsius to degrees in fahrenheit."""
celsius=48 #Degree temperature in celsius.
fahrenheit = (celsius*(9/5)) + 32 #Changes the degrees in celsius to degrees in fahrenheit.

print(f"{celsius} degrees celsius is {fahrenheit} in fahrenheit.") #The print command outputs a statement to the terminal.

"""The higher the degrees in celsius, the higher the degrees in fahrenheit.
1 degree higher in celsius is 1.8 degrees higher in fahrenheit."""
#Exercise 2

string=("StringExample")
integer=1
boolean=True
real=10.12

print(type(string))
print(type(integer))
print(type(boolean))
print(type(real))

print(f"{string} is a string which holds characters. {integer} is an integer which holds whole numbers. {real} is a float which holds numbers with a non-zero decimal. {boolean} is a boolean which holds either true or false.")

integer=str(integer)
"""There are all sorts of reasons you would need to change the variable type post-declaration. As variables change, something that is once more useful as a string could become something that must have calculations performed on it like an integer.
Most functions can only accept a certain type of variable so declaring the type for the purpose is important."""

#Exercise 3
name="Feeyah"
course="Computer Science"
favLanguage="Python"
movie="Spirited Away"

print("Hello! I'm "+name+" and I'm a person!")
text=("I study {} and my favourite programming language is {}")
print(text.format(course,favLanguage))
print(f"I love {movie}.")

alignment="alignment"
spacing="spacing"
real=round(real, 1)
print(f"This is a print statement to show my cool skills in {spacing:>10}, {alignment:^20} and precision formatting ({real})")

#Exercise 4
age=input("Please input your age.")
try:
    age=int(age)
except:
    age=0 #If input is not valid, the age is set to 0 so the rest of the program can run.

if(age<13):
    print("You are a child.")
elif(age<18):
    print("You are a teenager")
else:
    if(age<20):
        print("You are technically an adult")
    else:
        print("You are an adult (ew)")
