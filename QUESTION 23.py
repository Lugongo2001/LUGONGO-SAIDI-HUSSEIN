# Question 23: Overriding: Crop Water Needs
class Crop:
    def get_water_needs(self):
        return "Requires regular watering."
class Sugarcane(Crop):
    def get_water_needs(self):
        return "Requires high water volume."
class Sorghum(Crop):
    def get_water_needs(self):
        return "Is drought-resistant, requires minimal water."
print(f"Sugarcane water needs: {Sugarcane().get_water_needs()}")
print(f"Sorghum water needs: {Sorghum().get_water_needs()}")
print("-" * 20)
