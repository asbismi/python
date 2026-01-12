from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name: str, account_year: int):
        self.name = name
        self.account_year = account_year
    def account_age(self) -> int:
        current_year = 2025
        return current_year - self.account_year
    @abstractmethod
    def get_role(self) -> str:
        pass
class Admin(User):
    def get_role(self) -> str:
        return "Admin"

    def __str__(self) -> str:
        return f"Admin User: {self.name} (Account created in {self.account_year})"
class Guest(User):
    def get_role(self) -> str:
        return "Guest"

    def __str__(self) -> str:
        return f"Guest User: {self.name} (Account created in {self.account_year})"
admin_user = Admin("Alice", 2018)
guest_user = Guest("Bob", 2023)

# Demonstration
print(admin_user.get_role())
print(admin_user.account_age())
print(admin_user)

print()

print(guest_user.get_role())
print(guest_user.account_age())
print(guest_user)
