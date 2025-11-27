#Exercise 1
# 1. Create a List of Dictionaries
# This represents a database of students.
students = [
    {"name": "Alice", "score": 85, "passed": True},
    {"name": "Bob", "score": 40, "passed": False},
    {"name": "Charlie", "score": 92, "passed": True}
]
# 2. The Loop
# "student" is a temporary variable that holds ONE dictionary at a time.
print("--- Class Results ---")
for student in students:
    # 3. Access specific data using the ["keys"]
    name = student["name"]
    score = student["score"]
    # 4. Print it nicely
    print(f"Student: {name} | Score: {score}")
    if student["passed"]==True:
        print(f"{name} has passed!")
    else:
        print(f"{name} has failed.")
print("---------------------")

#Exercise 2
products=[
    {"item":"milk","price":0.90},
    {"item":"bread","price":1.20},
    {"item":"apple","price":0.50},
]

for product in products:
    print(f"The price of {product["item"]} is £{product["price"]:.2f}")

#Exercise 3
# This simulates data we might get from a User API
fake_api_data = {
    "status": "success",
    "total_results": 2,
    "users": [
        {"id": 1, "name": "John", "contact": {"email": "john@test.com"}},
        {"id": 2, "name": "Jane", "contact": {"email": "jane@test.com"}}
    ]
}
# HINT:
# 1. Access the "users" list first: fake_api_data["users"]
# 2. Access the second item (index 1): ... [1]
# 3. Access the "contact" dictionary: ... ["contact"]
# 4. Access the "email" key: ... ["email"]

user_list=fake_api_data["users"]
chosen_user=user_list[1]
chosen_contact=chosen_user["contact"]
print(chosen_contact["email"])

#Exercise 4-6
import requests # Import the tool to talk to the web
url = "https://official-joke-api.appspot.com/random_joke" #This website gives you a random joke every time it is opened so when accessed, it's different every time.
# 1. Send the request
print("Calling the server...")
try:
    response = requests.get(url,timeout=5) #Wait a maximum of 5 seconds.
    response.raise_for_status() #Checks for 404/500 errors automatically.
except requests.exceptions.ConnectionError:
    # This runs if your WiFi is off
    print("ERROR: No internet connection.")
except Exception as e:
    # This runs for any other error
    print(f"ERROR: Something went wrong: {e}")

response_dict=response.json() #Changes text to python dictionary.

print(response_dict["setup"])
import time
time.sleep(3)
print(response_dict["punchline"])

#Exercise 7
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true" #This website tells me information about the weather in Berlin
# 1. Send the request
print("Calling the server...")
try:
    response = requests.get(url,timeout=5) #Wait a maximum of 5 seconds.
    response.raise_for_status() #Checks for 404/500 errors automatically.
except requests.exceptions.ConnectionError:
    # This runs if your WiFi is off
    print("ERROR: No internet connection.")
except Exception as e:
    # This runs for any other error
    print(f"ERROR: Something went wrong: {e}")

weather=response.json() #Changes text to python dictionary.
weather_info=weather["current_weather"]
print(f"temperature:{weather_info["temperature"]}  windspeed:{weather_info["windspeed"]}")
if weather_info["temperature"]<10:
    print("It is cold, wear a coat.")
else:
    print("It is not cold enough to wear a coat.")

import datetime
with open("weather_log.txt","a") as file:
    date=datetime.datetime.now()
    date=date.strftime("%x")
    text=f"{weather_info["temperature"]} windspeed:{weather_info["windspeed"]} {date}"
    file.write(text)