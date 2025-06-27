# Question 28: Inheritance & Polymorphism: Pest Management
class Pest:
    def damage_report(self):
        print("Generic pest damage.")

class InsectPest(Pest):
    def damage_report(self):
        print("Insect pest damage: Chewing leaves, sucking sap.")
class FungalPest(Pest):
    def damage_report(self):
        print("Fungal pest damage: Leaf spots, wilting.")
class Crop:
    def __init__(self, name, pests=[]):
        self.name = name
        self.pests = pests
    def add_pest(self, pest):
        self.pests.append(pest)
    def generate_pest_report(self):
        print(f"Pest report for {self.name}:")
        for pest in self.pests:
            pest.damage_report()
crop = Crop("Maize")
crop.add_pest(InsectPest())
crop.add_pest(FungalPest())
crop.generate_pest_report()
print("-" * 20)
