# Question 29: Abstract Class & Inheritance: Water Management
class WaterSource(abc.ABC):
    @abc.abstractmethod
    def get_water(self, liters):
        pass
class Borehole(WaterSource):
    def __init__(self, max_daily_extraction):
        self.max_daily_extraction = max_daily_extraction
    def get_water(self, liters):
        if liters <= self.max_daily_extraction:
            print(f"Extracted {liters} liters from borehole.")
            return liters
        else:
            print("Exceeded daily extraction limit.")
            return 0
class River(WaterSource):
    def __init__(self, flow_rate):
        self.flow_rate = flow_rate
    def get_water(self, liters):
        print(f"Extracted {liters} liters from river.")
        return liters
borehole = Borehole(5000)
river = River(1000) # liters per hour (example)
print("Question 29:")
print(f"Borehole water: {borehole.get_water(3000)} liters")
print(f"River water: {river.get_water(2000)} liters")
print("-" * 20)
