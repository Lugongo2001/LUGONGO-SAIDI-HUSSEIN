#Question 12: Crop Growth Cycle Class

import datetime
class Crop:
    def __init__(self, name, planting_date, days_to_maturity):
        self.name = name
        self.planting_date = planting_date # datetime object
        self.days_to_maturity = days_to_maturity
    def calculate_harvest_date(self):
        harvest_date = self.planting_date + datetime.timedelta(days=self.days_to_maturity)
        return harvest_date
planting_date = datetime.date(2024, 3, 15)
my_crop = Crop("Maize", planting_date, 120)
harvest_date = my_crop.calculate_harvest_date()
print(f"Expected harvest date for {my_crop.name}: {harvest_date}")
