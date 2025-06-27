#Question 15: Irrigation Pump Calculator
class IrrigationPump:
    def __init__(self, pump_type, flow_rate):
        self.pump_type = pump_type
        self.flow_rate = flow_rate # liters/minute
    def calculate_water_pumped(self, time_hours):
        total_liters = self.flow_rate * time_hours * 60
        total_cubic_meters = total_liters / 1000
        return total_cubic_meters
my_pump = IrrigationPump("Centrifugal", 1000)
water_pumped = my_pump.calculate_water_pumped(5) # 5 hours
print(f"Total water pumped: {water_pumped:.2f} cubic meters")
