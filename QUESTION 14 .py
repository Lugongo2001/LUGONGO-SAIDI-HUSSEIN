#Question 14: Farm Animal Class
class FarmAnimal:
    def __init__(self, species, age, purpose):
        self.species = species
        self.age = age
        self.purpose = purpose
    def get_details(self):
        return f"Species: {self.species}, Age: {self.age}, Purpose: {self.purpose}"
cow = FarmAnimal("Cow", 3, "Dairy")
chicken = FarmAnimal("Chicken", 1, "Meat")
print(cow.get_details())
print(chicken.get_details())
