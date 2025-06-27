#Question 19: Abstract Class: Agricultural Sensor
import abc
import random
class AgriculturalSensor(abc.ABC):
    @abc.abstractmethod
    def read_data(self):
        pass
class SoilMoistureSensor(AgriculturalSensor):
    def read_data(self):
        return random.uniform(0, 100) # Percentage
class AirTemperatureSensor(AgriculturalSensor):
    def read_data(self):
        return random.uniform(15, 35) # Celsius
soil_sensor = SoilMoistureSensor()
temp_sensor = AirTemperatureSensor()
print(f"Soil moisture: {soil_sensor.read_data():.2f}%")
print(f"Air temperature: {temp_sensor.read_data():.2f}°C")
