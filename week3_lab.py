"""Loops and Stuff!"""

for i in range(20): #Prints numbers 1 to 10, each on a new line.
    if((i+1)%2==0):
        print(i+1)

numList=[10.1,20.3,40.7,9.9]
total=0.0
for num in numList:
    total=total+num

print(f"The numbers added together are equal to {total:.2f}")