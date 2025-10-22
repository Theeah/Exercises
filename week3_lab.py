"""Loops and Stuff!"""

for i in range(20): #Prints numbers 1 to 10, each on a new line.
    if((i+1)%2==0):
        print(i+1)

numList=[10.1,20.3,40.7,9.9]
total=0.0
for num in numList:
    total=total+num

print(f"The numbers added together are equal to {total:.2f}")

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

loop=True
while(loop==True):
    print("What would you like to do?")
    print("Type 1 to add some numbers!")
    print("Type 2 to subtract some numbers!")
    print("Type 3 to exit the calculator!")
    decision=input()
    if(decision=="3"):
        print("Thank you for using the calculator!")
        loop=False
    elif(decision=="1"):
        num1=0
        num2=0
        try:
            num1=int(input("Input your first number"))
            num2=int(input("Input your second number"))
        except:
            print("Fail.")
        
        print(f"The answer is {num1+num2}")
        print()
    elif(decision=="2"):
        num1=0
        num2=0
        try:
            num1=int(input("Input your first number"))
            num2=int(input("Input your second number"))
        except:
            print("Fail.")
        
        print(f"The answer is {num1-num2}")
        print()
    else:
        print()