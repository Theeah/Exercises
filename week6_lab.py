#Exercise 1
log_data = "SCORE:Player_1:2500"
parsed_data=log_data.split(":")
print(parsed_data)
print(parsed_data[1])
print(parsed_data[2])

#Exercise 2
questions = ["What is 2+2?", "What is the capital of France?", "What keyword defines a function?"]
answers = ["4", "Paris", "def"]
score=0
for i in range(len(questions)):
    print(questions[i])
    player_ans=input()
    if player_ans==answers[i]:
        print("Correct!")
        score=score+1
    else:
        print("Wrong.")

print(score)

#Exercise 3
phonebook={}
phonebook["Alex"]="Very real phone number"
phonebook["Zahari"]="Super real phone number"
name=input("Who do you want to look up?")
print(phonebook[name])
phonebook["Feeyah"]="Fake number"

for name, number in phonebook.items():
    print(f"{name} {number}")