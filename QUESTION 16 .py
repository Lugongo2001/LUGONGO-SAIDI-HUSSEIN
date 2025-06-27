#Question 16: Inheritance: Farm Equipment
class FarmEquipment:
    def __init__(self, name, purchase_price):
        self.name = name
        self.purchase_price = purchase_price
class Tractor(FarmEquipment):
    def __init__(self, name, purchase_price, horsepower):
        super().__init__(name, purchase_price)
        self.horsepower = horsepower
class Harvester(FarmEquipment):
    def __init__(self, name, purchase_price, cutting_width):
        super().__init__(name, purchase_price)
        self.cutting_width = cutting_width
tractor = Tractor("John Deere", 50000, 150)
harvester = Harvester("Claas", 75000, 6)
print(f"Tractor Horsepower: {tractor.horsepower}")
print(f"Harvester Cutting Width: {harvester.cutting_width}")
