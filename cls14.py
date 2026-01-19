import random
import math

names_input = input("Enter the names of invited guests (comma-separated): ")

names = [name.strip() for name in names_input.split(",") if name.strip()]

unique_names = list(dict.fromkeys(names))

if not unique_names:
    print("No valid names were entered.")
else:

    chosen_name = random.choice(unique_names)

    reversed_name = chosen_name[::-1]

    total_unique = len(unique_names)

    rounded_sqrt = round(math.sqrt(total_unique))

    print("\nUnique names:", unique_names)
    print("Chosen name:", chosen_name)
    print("Reversed name:", reversed_name)
    print("Total number of unique names:", total_unique)
    print("Rounded square root of total:", rounded_sqrt)
