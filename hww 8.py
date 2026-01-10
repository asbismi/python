# Base class
class Account:
    def __init__(self, name, balance):
        self._name = name        # protected attribute
        self._balance = balance # protected attribute

    # Operator overloading for +
    def __add__(self, other):
        return self._balance + other._balance


# SavingsAccount class
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05   # 5% interest


# CurrentAccount class
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02   # 2% interest


# Main part of the program
if __name__ == "__main__":

    # Creating account objects
    savings = SavingsAccount("Ravi", 10000)
    current = CurrentAccount("Anjali", 15000)

    # Display Savings Account details
    print("Savings Account Details")
    print("Name:", savings._name)
    print("Balance:", savings._balance)
    print("Interest:", savings.calculate_interest())
    print()

    # Display Current Account details
    print("Current Account Details")
    print("Name:", current._name)
    print("Balance:", current._balance)
    print("Interest:", current.calculate_interest())
    print()

    # Total balance using operator overloading
    total_balance = savings + current
    print("Total Balance (Savings + Current):", total_balance)
