# Question 17: Inheritance: Crop Types
class Crop:
    def planting_instructions(self):
        print("Generic planting instructions: Prepare soil, plant seeds, water regularly.")
class CerealCrop(Crop):
    def __init__(self, name, grain_type):
        self.name = name
        self.grain_type = grain_type
class LegumeCrop(Crop):
    def __init__(self, name, nitrogen_fixing):
        self.name = name
        self.nitrogen_fixing = nitrogen_fixing
wheat = CerealCrop("Wheat", "Hard Red Winter")
soybean = LegumeCrop("Soybean", True)
print("Question 17:")
print("Wheat Planting Instructions:")
wheat.planting_instructions()
print("Soybean Planting Instructions:")
soybean.planting_instructions() # Uses the generic instructions from the parent class
print("-" * 20)
