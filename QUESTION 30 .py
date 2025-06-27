#Question 30: Full System Simulation (Simplified for brevity)
class FarmAnimal:
    def __init__(self, species):
        self.species = species
class Crop:
    def __init__(self, name):
        self.name = name
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.crops = {}
    def add_animal(self, animal):
        self.animals.append(animal)
    def plant_crop(self, field_name, crop):
        self.crops[field_name] = crop
farm = Farm("Happy Acres")
farm.add_animal(FarmAnimal("Cow"))
farm.plant_crop("Field A", Crop("Maize"))
print("Question 30:")
print(f"Farm Name: {farm.name}")
print(f"Animals: {[animal.species for animal in farm.animals]}")
print(f"Crops: {list(farm.crops.keys())}")
