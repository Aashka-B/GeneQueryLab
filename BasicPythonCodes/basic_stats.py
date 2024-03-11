"""
A python program that calculates descriptive statistics
for numbers found in columns of a given input file.
"""

# Importing the necessary modules
import sys
import math

# Defining global variables
input_file = sys.argv[1]
column_to_parse = int(sys.argv[2])

def calculate_statistics():
    """

    :return:
    """
    # Lists to store numeric values from the specified column
    numbers = []
    valid_numbers = []

    # Open the input file using 'with' for safe file handling
    with open(input_file, 'r', encoding="utf-8") as infile:
        for line_num, line in enumerate(infile, start=1):
            try:
                # Split the line into columns based on tabs
                num = line.split('\t')[column_to_parse]
                numbers.append(num)
                num = float(num)

                if not math.isnan(num):
                    valid_numbers.append(num)

            # Error message incase of a Value Error
            except ValueError:
                print(f"\nSkipping line number {line_num} : "
                      f"could not convert string to float: '{num}'")

            # Error message for an Index Error
            except IndexError:
                print(f"\nExiting: There is no valid 'list index' in column {column_to_parse}"
                      f" in line {line_num} in file: {input_file}")
                sys.exit(1)

    # Error message for invalid column number
    if not valid_numbers:
        print(f"\nError: There were no valid number(s) in column {column_to_parse} "
              f"in file: {input_file}")
        sys.exit(1)

    # Calculating average, maximum, and minimum
    average = sum(valid_numbers) / len(valid_numbers)
    maximum = max(valid_numbers)
    minimum = min(valid_numbers)

    # Calculating variance with exception
    if (len(valid_numbers) - 1) != 0:
        variance = sum((x - average) ** 2 for x in valid_numbers) / (len(valid_numbers) - 1)
    else:
        variance = 0

    # Calculating standard deviation
    std_dev = math.sqrt(variance)

    # Calculating median
    sorted_num = sorted(valid_numbers)
    if len(valid_numbers) % 2 == 1:
        median = sorted_num[len(valid_numbers) // 2]
    else:
        median = (sorted_num[len(valid_numbers) // 2 - 1] + sorted_num[len(valid_numbers) // 2]) / 2

    # Printing the results with proper formatting
    print("\r")
    print(f"    Column: {column_to_parse}\n")
    print(f"        Count     =   {len(numbers):.3f}")
    print(f"        ValidNum  =   {len(valid_numbers):.3f}")
    print(f"        Average   =   {average:.3f}")
    print(f"        Maximum   =   {maximum:.3f}")
    print(f"        Minimum   =   {minimum:.3f}")
    print(f"        Variance  =   {variance:.3f}")
    print(f"        Std Dev   =   {std_dev:.3f}")
    print(f"        Median    =   {median:.3f}")

# Calling the function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python stats_in_python.py input_file.txt column_number")
        sys.exit(1)

    calculate_statistics()
