class UserInputError(Exception):
    """Error for when the user fails to input something."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def safe_input(prompt: str) -> str:
    """Returns the input.
    Will return an empty string if a keyboard interrupt happens."""
    try:
        inp = input(prompt)
    except(KeyboardInterrupt, EOFError):
        print("Input Cancelled.")
        return None #Returns None to signal error.
    else:
        return inp

def get_non_empty_string(prompt: str):
    """Returns a string that is not empty"""
    max_attempts = 10
    attempts = 0
    while attempts <= max_attempts:
        inp = safe_input(prompt)
        if not inp:
            return None # Input cancelled
        inp = inp.strip()
        if inp == "":
            print("Input cannot be empty.")
            attempts = attempts + 1
            continue
        return inp
    print("Max attempts exceeded.")
    return None #Error return

def get_valid_integer(
    prompt: str,
    min_value: int,
    max_value: int
) -> int:
    """Gets an input and checks it is a proper integer.
    Returns a valid integer between the two values."""
    max_attempts = 10
    attempts = 0
    while attempts <= max_attempts:
        inp = get_non_empty_string(prompt)
        if not inp:
            return None #If there has been a program-ending error, it should be carried through.
        try:
            inp = int(inp)
        except ValueError:
            print("Input must be a number.")
            attempts = attempts + 1
            continue
        if inp < min_value:
            print(f"Input must be higher than {min_value}")
            #raise Exception(UserInputError("Ha, failure."))
        elif inp > max_value:
            print(f"Input must be below {max_value}")
        else:
            return inp
        attempts = attempts + 1
    print("Max attempts exceeded.")
    return None #Error return

def get_valid_float(
    prompt: str,
    min_value: int,
    max_value: int
) -> int:
    """Gets an input and checks it is a proper integer.
    Returns a valid integer between the two values."""
    max_attempts = 10
    attempts = 0
    while attempts <= max_attempts:
        inp = get_non_empty_string(prompt)
        if not inp:
            return None #If there has been a program-ending error, it should be carried through.
        try:
            inp = float(inp)
        except ValueError:
            print("Input must be a float")
            attempts = attempts + 1
            continue
        if inp < min_value:
            print(f"Input must be higher than {min_value}")
        elif inp > max_value:
            print(f"Input must be below {max_value}")
        else:
            return inp
        attempts = attempts + 1
    print("Max attempts exceeded.")
    return None #Error return

def get_choice(prompt: str, list_of_choices: list[str]) -> str:
    """Gets an input and checks it is in list_of_choices.
    If not, an error is outputted and the method repeats."""
    max_attempts = 10
    attempts = 0
    while attempts <= max_attempts:
        choice = get_non_empty_string(prompt)
        if not choice:
            return None #If there has been a program-ending error, it should be carried through.
        
        for item in list_of_choices:
            print (item)
            print (choice)
            if choice == item:
                return choice
        #If program still runs after loop, the choice was not valid, since it has not been returned.
        print("Please enter a valid choice.")
        attempts = attempts + 1

    print("Max attempts exceeded.")
    return None #Error return

def get_formatted_date() -> str:
    """Returns a formatted date in the form DD-MM-YYYY"""
    day = get_valid_integer("Please enter the day number.", 0, 30)
    if (day<10):
        day = f"0{str(day)}" #Formatting so it's 03-11-2026 instead of 3-11-2026
    else:
        day = str(day)
    month = get_valid_integer("Please enter the month number.", 1, 12)
    if month<10:
        month = f"0{str(month)}" #Formatting so it's 13-01-2026 instead of 13-1-2026
    else:
        month = str(month)
    year = get_valid_integer("Please enter the year.", 2000, 2050)
    year = str(year)
    return f"{day}-{month}-{year}"

def add_expense(expense_list: list[dict]) -> list[dict]:
    name = get_non_empty_string("Please enter the name.")
    date = get_formatted_date()
    category = get_choice("What type of expense is this?", ["food", "clothes", "luxuries", "other"])
    amount = get_valid_float("Please enter the amount.")
    new_expense = {"name": name, "date": date, "category": category, "amount": amount}
    expense_list.append(new_expense)
    return expense_list

def display_sum(expense_list: list[dict]):
    total = 0
    for item in expense_list:
        total = total + item["amount"]

def filter_expenses(expense_list: list[dict], category: str):
    for item in expense_list:
        if item["category"] == category:
            print(item)