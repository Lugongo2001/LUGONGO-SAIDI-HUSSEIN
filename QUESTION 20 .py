# Question 20: Inheritance: Livestock
class Livestock:
    def __init__(self, species, weight):
        self.species = species
        self.weight = weight
class Cattle(Livestock):
    def calculate_feed_ratio(self):
        return self.weight * 0.02
class Poultry(Livestock):
    def calculate_feed_ratio(self):
        return self.weight * 0.05
cow = Cattle("Angus", 600)
chicken = Poultry("Leghorn", 2)
print(f"Cattle feed ratio: {cow.calculate_feed_ratio()} kg")
print(f"Poultry feed ratio: {chicken.calculate_feed_ratio()} kg")
print("-" * 20)
