# Question 25: Overriding: Harvesting Methods
class Plant:
    def harvest(self):
        print("Generic harvesting method.")
class FruitTree(Plant):
    def harvest(self):
        print("Harvest by picking fruits carefully.")
class RootVegetable(Plant):
    def harvest(self):
        print("Harvest by digging up from the soil.")
plants = [FruitTree(), RootVegetable()]
for plant in plants:
    plant.harvest()
print("-" * 20)
