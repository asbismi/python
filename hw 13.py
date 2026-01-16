filename = "students.txt"

# Step 1: Show existing names if the file exists
try:
    with open(filename, "r") as file:
        print("Existing student names:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("No existing file found. A new file will be created.")

# Step 2: Ask how many names to add
num_students = int(input("\nHow many student names do you want to add? "))

# Step 3: Append new names to the file
with open(filename, "a") as file:
    for i in range(num_students):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

# Step 4: Display updated list of names
print("\nUpdated list of all student names:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
