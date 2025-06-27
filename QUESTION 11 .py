# Question 11: Tractor Object Modeling
class Tractor:
    def __init__(self, model, horsepower, fuel_capacity):
        self.model = model
        self.horsepower = horsepower
        self.fuel_capacity = fuel_capacity
    def display_info(self):
        print(f"Tractor Model: {self.model}")
        print(f"Horsepower: {self.horsepower}")
        print(f"Fuel Capacity: {self.fuel_capacity} liters")
tractor = Tractor("Massey Ferguson 240", 80, 100)
tractor.display_info()
print("-" * 20)
