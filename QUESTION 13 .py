#Question 13: Soil Sample Analysis Class
class SoilSample:
    def __init__(self, sample_id, ph_level, organic_matter):
        self.sample_id = sample_id
        self.ph_level = ph_level
        self.organic_matter = organic_matter
    def get_fertility_status(self):
        if 6.0 <= self.ph_level <= 7.0 and self.organic_matter > 2.5:
            return "High"
        elif (6.0 <= self.ph_level <= 7.0) or (self.organic_matter > 2.5):
            return "Medium"
        else:
            return "Low"
sample1 = SoilSample("A123", 6.5, 3.0)
print(f"Fertility status of {sample1.sample_id}: {sample1.get_fertility_status()}")
