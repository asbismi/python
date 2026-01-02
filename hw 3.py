
web_dev = ["Asha", "Rahul", "Neha"]
data_science = ["Kiran", "Meera", "Arjun"]
ui_ux = ["Anita", "Sonal", "Vivek"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("Rohit")

data_science.insert(1, "Pooja")

ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

print("First two Web Dev participants:", web_dev[:2])

name_lengths = [len(name) for name in data_science_copy]
print("Lengths of names in copied Data Science list:", name_lengths)

is_asha_present = (
    "Asha" in web_dev or
    "Asha" in data_science or
    "Asha" in ui_ux
)
print("Is Asha present in any workshop?", is_asha_present)

first_participants = (
    web_dev[0],
    data_science_copy[0],
    ui_ux[0]
)

print("First participants tuple:", first_participants)
