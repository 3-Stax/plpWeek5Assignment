class Car:
    def __init__(self, make, model, year, color, max_speed):
        self._make = make  # Encapsulated with '_' (protected)
        self._model = model
        self._year = year
        self._color = color
        self._max_speed = max_speed
        self._current_speed = 0
        self._is_running = False

    # Encapsulation: Getters and Setters
    @property
    def make(self):
        return self._make
    
    @property
    def current_speed(self):
        return self._current_speed

    # Methods to bring the car to life
    def start(self):
        if not self._is_running:
            self._is_running = True
            print(f"{self._make} {self._model} engine started. Vroom!")
        else:
            print("Car is already running.")

    def accelerate(self, speed_increase):
        if self._is_running:
            new_speed = self._current_speed + speed_increase
            self._current_speed = min(new_speed, self._max_speed)
            print(f"Accelerating to {self._current_speed} km/h")
        else:
            print("Start the car first!")

    def brake(self, speed_decrease):
        new_speed = self._current_speed - speed_decrease
        self._current_speed = max(new_speed, 0)
        print(f"Slowing down to {self._current_speed} km/h")

    def stop(self):
        self._current_speed = 0
        self._is_running = False
        print("Car has stopped.")

    def __str__(self):
        return (f"{self._year} {self._make} {self._model} (Color: {self._color}, "
                f"Max Speed: {self._max_speed} km/h)")


# Inheritance - ElectricCar is a subclass of Car
class ElectricCar(Car):
    def __init__(self, make, model, year, color, max_speed, battery_capacity):
        super().__init__(make, model, year, color, max_speed)
        self._battery_capacity = battery_capacity  # kWh
        self._remaining_charge = 100  # Percentage

    # Polymorphism: Override the start method
    def start(self):
        if not self._is_running:
            self._is_running = True
            print(f"{self._make} {self._model} started silently. ⚡")
        else:
            print("Electric car is already running.")

    # Additional method specific to ElectricCar
    def charge(self, percentage):
        self._remaining_charge = min(100, self._remaining_charge + percentage)
        print(f"Battery charged to {self._remaining_charge}%")

    def __str__(self):
        return (super().__str__() + 
                f", Battery: {self._battery_capacity}kWh, Charge: {self._remaining_charge}%")


# Demonstration
if __name__ == "__main__":
    # Create instances
    my_car = Car("Toyota", "Camry", 2022, "Blue", 180)
    my_tesla = ElectricCar("Tesla", "Model S", 2023, "Red", 250, 100)

    # Interact with the cars
    print(my_car)
    my_car.start()
    my_car.accelerate(50)
    my_car.brake(20)
    my_car.stop()

    print("\n" + "="*50 + "\n")

    print(my_tesla)
    my_tesla.start()  # Polymorphism in action - different start behavior
    my_tesla.accelerate(70)
    my_tesla.charge(30)
