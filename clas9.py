from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year
    def years_on_platform(self):
        current_year = 2025
        return current_year - self.join_year
    @abstractmethod
    def get_role(self):
        pass
class Customer(User):
    def get_role(self):
        return "Customer"

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Role: {self.get_role()}, "
            f"Years on platform: {self.years_on_platform()}"
        )
class Vendor(User):
    def get_role(self):
        return "Vendor"

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Role: {self.get_role()}, "
            f"Years on platform: {self.years_on_platform()}"
        )
customer = Customer("Rahul", 2020)
vendor = Vendor("Anita", 2017)
print(customer)
print(vendor)
