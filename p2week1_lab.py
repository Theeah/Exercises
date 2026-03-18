from __future__ import annotations

def parse_numbers(text: str):
    """Parse comma-separated numbers into floats."""
    raw_tokens = [t.strip() for t in text.split(",")] #Splits the text and saves as raw_tokens
    tokens = [t for t in raw_tokens if t != ""] #Loops through the split text and saves a value if it is not empty.

    if not tokens: #Happens if there are no tokens
        raise ValueError("No numbers provided. Example input: 1, 2, 3")

    values: list[float] = [] #Basically values = but it sets what type values should be.
    for t in tokens:
        try:
            values.append(float(t))
        except ValueError:
            print(f"Invalid number token: {t!r}")
            values = [] #returns empty values as a signal that something has gone wrong.

    return values

def summary(values: list[float]):
    num_of_values = len(values)
    sum = 0
    for item in values:
        sum = sum + item
    average = sum / num_of_values
    med = median(values)
    summary = {"count":num_of_values,"sum":sum,"avg":average,"median":med,"max":sorted(values)[0],"min":sorted(values)[num_of_values-1]}
    return summary

def format_summary(summary):
    for key, value in summary.items():
        print(f"{key}: {value}")

def read_text_file(path: str):
    """Reads a file when given the relative path"""
    try:
        with open(path) as f:
            print(f.readlines())
    except FileNotFoundError as e:
        raise FileNotFoundError(f"That file path was not found") from e
    except Exception as e:
        raise e

def median(values: list[float]):
    """Returns the median of a list of floats."""
    sorted_values=sorted(values)
    mid=len(sorted_values) // 2
    median = sorted_values[mid]
    if mid % 2 == 1:
        median = (sorted_values[mid] + sorted_values[mid-1]) / 2
    
    return median

def main():
        try:
            data = input("Enter comma-separated numbers: ")
            nums = parse_numbers(data)
            if nums != []: #When an error has happened, we want the program to restart so it doesn't finish running.
                summ = summary(nums)
                format_summary(summ)
                #file_path = input("Please enter the file path to read from.")
                #read_text_file(file_path)
            choice = input("Would you like to restart?")
            if choice.lower() == "yes":
                main()
        except ValueError as e:
            print(f"Error: {e}")
            main()

if __name__=="__main__":
    main()