import random
import math

names_input = input("Enter customer names (comma-separated): ")

names = [name.strip() for name in names_input.split(",") if name.strip()]

unique_names = list(dict.fromkeys(names))

if len(unique_names) < 2:
    print("At least 2 unique participants are required for the lucky draw.")
else:

    random.shuffle(unique_names)


    winners = random.sample(unique_names, 2)

    reversed_winners = [winner[::-1] for winner in winners]

    total_participants = len(unique_names)

    rounded_sqrt = round(math.sqrt(total_participants))

    print("\n🎉 Lucky Draw Results 🎉")
    print("Winners (reversed names):")
    print("Winner 1:", reversed_winners[0])
    print("Winner 2:", reversed_winners[1])
    print("\nTotal unique participants:", total_participants)
    print("Rounded square root of participants:", rounded_sqrt)
