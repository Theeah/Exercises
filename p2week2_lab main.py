from p2week2_lab import get_non_empty_string
from p2week2_lab import get_valid_integer
from p2week2_lab import get_choice
from p2week2_lab import add_expense
from p2week2_lab import filter_expenses
from p2week2_lab import display_sum

def main():
    user = get_non_empty_string("Please enter a username.")
    age = get_valid_integer("Please enter an age.", 0, 120)
    role = get_choice("What is your role?", ['admin', 'user', 'guest'])
    opinion = get_choice("Do you like flowers?", ['yes', 'no', 'y', 'n'])
    if not user or not age or not role or not opinion:
        print("Summary cannot be generated")
    else:
        print(f"{user} is {age} years old and works as {role}. When asked if they like flowers, they simply replied '{opinion}'")

def expense_tracker_main():
    choice = "0"
    expense_list = []
    while choice != "4":
        choice = get_choice("What would you like to do? \n [1] View sum \n [2] View filtered expense \n [3] Add a new expense \n [4] Exit", ["1", "2", "3", "4"])
        if not choice:
            break
        if choice == "1":
            display_sum(expense_list)
        elif choice == "2":
            category = get_choice("What would you like to filter by?", ["food", "clothes", "luxuries", "other"])
            filter_expenses(expense_list, category)
        elif choice == "3":
            add_expense(expense_list)

expense_tracker_main()