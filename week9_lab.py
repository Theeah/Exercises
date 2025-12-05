#Exercise 1
def add_contact(contacts):
    contact_name = input("What is the name of the new contact?")
    contact_number = input("What is the number?")
    contacts.append({"contact_name":contact_name,"contact_number":contact_number})
    return contacts

def view_contacts(contacts):
    print(contacts)

def delete_contact(contacts):
    name = input("Whose contact do you want to delete?")
    count = 0
    for item in contacts:
        if item["contact_name"] == name:
            contacts.pop(count)
        count = count + 1
            
def main_menu():
    contacts=[]
    print("What would you like to do?")
    print("[1] Add a new contact")
    print("[2] View current contacts")
    print("[3] Delete a contact")
    print("[4] Quit")
    choice = input()
    
    if choice == "1":
        contacts=add_contact(contacts)
        main_menu()
    elif choice == "2":
        view_contacts(contacts)
        main_menu()
    elif choice == "3":
        delete_contact(contacts)
        main_menu()
    elif choice == "4":
        print("Closing...")
    else:
        print("Error: Invalid choice")

contacts = []
main_menu()

#Exercise 2
import json
# This simulates raw JSON data downloaded from a game server
raw_server_data = """
[
    {"id": 101, "name": "Slay the Dragon", "reward": 500, "status":
"Active", "tags": ["Combat", "Hard"]},
    {"id": 102, "name": "Find the Lost Cat", "reward": 50, "status":
"Active", "tags": ["Fetch", "Easy"]},
    {"id": 103, "name": "Retrieve the Sword", "reward": 1000, "status":
"Completed", "tags": ["Story", "Hard"]},
    {"id": 104, "name": "Defend the Gate", "reward": 300, "status":
"Active", "tags": ["Combat", "Medium"]}
]
"""

def filter_quests(quest_list, min_gold):
    """
    Returns a list of quest names that are 'Active' and have a reward >=
    min_gold.
    """
    matching_quests = [] # Create an empty list to store results
    for item in quest_list:
        if item["status"]=="Active":
            if item["reward"]>=min_gold:
                matching_quests.append(item["name"])

    # 1. Loop through quest_list
    # 2. Check if status is 'Active' AND reward >= min_gold
    # 3. If true, append the quest["name"] to matching_quests

    return matching_quests

def calculate_total_gold(quest_list):
    """
    Returns the sum of rewards for ALL 'Active' quests in the list.
    """
    active_quests=filter_quests(quest_list, 0) #We want all active quests so min_gold is 0.
    total = 0
    for item in quest_list: #For all items..
        for quest_name in active_quests: #Checks against each quest_name.. 
            if item["name"]==quest_name: #If they are the same, it is a relevant quest.
                total=total+item["reward"]
    
    return total

# --- Main Program Execution ---
print("--- QUEST BOARD SYSTEM ---")
# 1. Parse the JSON string into a Python List of Dictionaries
data = json.loads(raw_server_data)
# 2. Call the filter function (Find active quests worth 100 gold or more)
high_value_quests = filter_quests(data, 100)
# 3. Print the results
print(f"High Value Quests found: {high_value_quests}")
# 4. Calculate total potential earnings
potential_earnings = calculate_total_gold(data)
print(f"Total gold available in Active quests: {potential_earnings}")
# EXPECTED OUTPUT: 850