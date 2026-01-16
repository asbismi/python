filename = "items.txt"

# Ask the user for a new item
item = input("Enter the name of the new item: ")

# Open file in append mode (creates file if it doesn't exist)
with open(filename, "a") as file:
    file.write(item + "\n")

# Read and display all items from the file
print("\nList of items:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
