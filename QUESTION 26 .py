# Question 26: Farm Management System: Classes
class Crop:
    def __init__(self, name, yield_per_hectare):
        self.name = name
        self.yield_per_hectare = yield_per_hectare
class Field:
    def __init__(self, size_in_hectares, crops=[]):
        self.size_in_hectares = size_in_hectares
        self.crops = crops
    def add_crop(self, crop):
        self.crops.append(crop)
    def get_total_yield(self):
        total_yield = sum(crop.yield_per_hectare * self.size_in_hectares for crop in self.crops)
        return total_yield
field = Field(5)
field.add_crop(Crop("Maize", 5))
field.add_crop(Crop("Beans", 3))
print(f"Total yield: {field.get_total_yield()} tonnes")
print("-" * 20)
