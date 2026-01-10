# Base class
class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id  # Protected attribute
        self._base_rate = base_rate    # Protected attribute

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: ${self._base_rate:.2f}"

    def rental_charge(self):
        # Placeholder to be overridden by subclasses
        return 0.0


# Subclass for Car
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats  # Number of seats

    def rental_charge(self):
        # Rental charge = base_rate * number of seats
        return self._base_rate * self.num_seats


# Subclass for Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type  # Type of bike

    def rental_charge(self):
        # Rental charge = base_rate * 0.5
        return self._base_rate * 0.5


# Polymorphic function to calculate rental
def calculate_rental(vehicle):
    return vehicle.rental_charge()


# Main program
if __name__ == "__main__":
    # Create a Car object
    car1 = Car("CAR001", 100.0, 4)

    # Create a Bike object
    bike1 = Bike("BIKE001", 50.0, "Scooter")

    # Display details and rental charges
    print("Car Details:")
    print(car1.display_details())
    print(f"Rental Charge: ${calculate_rental(car1):.2f}\n")

    print("Bike Details:")
    print(bike1.display_details())
    print(f"Rental Charge: ${calculate_rental(bike1):.2f}")
