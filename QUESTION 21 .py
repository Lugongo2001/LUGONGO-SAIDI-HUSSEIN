#Question 21: Polymorphism: Farm Vehicle Operation
class FarmVehicle:
    def start_engine(self):
        print("Generic engine starting sequence")
class Tractor(FarmVehicle):
    def start_engine(self):
        print("Tractor engine starting sequence")

class Harvester(FarmVehicle):
    def start_engine(self):
        print("Harvester engine starting sequence")
vehicle = FarmVehicle()
tractor = Tractor()
harvester = Harvester()
vehicle.start_engine()
tractor.start_engine()
harvester.start_engine()
