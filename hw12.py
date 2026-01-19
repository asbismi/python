try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

    if not name or not feedback:
        raise ValueError("Name and feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

except ValueError as e:
    print(f"\nError: {e}")

finally:
    print("\nThank you for visiting our restaurant!")
