from abc import ABC, abstractmethod

# Abstract Base Class (Ensures all vehicles implement move())
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"{self.name}"

# Concrete Classes (Each defines move() differently)
class Car(Vehicle):
    def move(self):
        return f"🚗 {self.name} is driving on the road!"

class Plane(Vehicle):
    def move(self):
        return f"✈️ {self.name} is flying in the sky!"

class Boat(Vehicle):
    def move(self):
        return f"⛵ {self.name} is sailing on the water!"

class Bicycle(Vehicle):
    def move(self):
        return f"🚲 {self.name} is pedaling on the bike path!"

# Demo
if __name__ == "__main__":
    vehicles = [
        Car("Toyota Camry"),
        Plane("Boeing 747"),
        Boat("Sailboat"),
        Bicycle("Mountain Bike")
    ]

    for vehicle in vehicles:
        print(vehicle.move())  # Same method, different behaviors!
