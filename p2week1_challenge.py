def validate_num(num: str) -> float: #The extra unnecessary annotations are type hints. Use them, even if you don't like it.
    """Validates the price input so that it is:
    A number
    Above 0
    Below (or equal to) 1000"""
    if num == "":
        print("Price is required.")
        return ""
    else:
        try:
            num = float(num)
        except ValueError:
            raise ValueError("Price must be a number.")
        if num <= 0:
            print("Price must be above 0.") #Violation of the rules but Idk what else to do.
            return ""
        elif num > 1000:
            print("Price must be below or including 1000.") #Violation of the rules but Idk what else to do.
            return ""
        else:
            return f"{num:.2f}"

def main():
    num = input("Please input a price.")
    print(validate_num(num))
    

if __name__ == "__main__":
    main()