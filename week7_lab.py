#Exercise 1
print("Please write your diary entry")
entry=input()
with open("diary.txt","a") as file:
    file.write(entry+"\n")

print() #Seperate the input entry from the reading.

with open("diary.txt","r") as file:
    diaryText=file.read()
    print(diaryText)

#Exercise 2
import csv

grades={"Alice":[85,90,92],
        "Bob":[78,81,85],
        "Charlie":[95,100,98]}

with open("grades.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name", "Score 1", "Score 2", "Score 3"])
    for name,scores in grades.items():
        scores=grades[name]
        text=name,scores[0],scores[1],scores[2]
        writer.writerow(text)

with open("grades.csv","r",newline="") as file:
    reader=csv.reader(file)
    next(reader) #Skips header line
    for row in reader:
        score1=int(row[1])
        score2=int(row[2])
        score3=int(row[3])
        average=(score1+score2+score3)/3
        print(f"{row[0]} has an average score of {average}")

#Exercise 3
import json

inventory = [
{"id": 1, "item": "Potion", "cost": 50},
{"id": 2, "item": "Shield", "cost": 150}
]

def save_inventory():
    with open("save_game.json","w") as file:
        json.dump(inventory,file,indent=4)
    
def load_inventory():
    with open("save_game.json","r") as file:
        saved_inventory=json.load(file)
        return saved_inventory

save_inventory()
print(load_inventory())