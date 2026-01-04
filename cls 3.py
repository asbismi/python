fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
bevarages = ["water", "juice", "soda"]
fruits.append("orange")
vegetables.insert(1, "cabbage")
bevarages.pop()
inventory = [fruits, vegetables, bevarages]
print("first two fruits:", fruits[:2])
print("last vegetable:", vegetables[-1])
fruit_name_lengths = [len(fruit) for fruit in fruits]
print("Lengths of fruit names:", fruit_name_lengths)
print("is water in bevarages?", "water" in bevarages)
first_items = (
    fruits[0],
    vegetables[0],
    bevarages[0]
)
print("Tuple of first items:", first_items)
print("inventory:", inventory)