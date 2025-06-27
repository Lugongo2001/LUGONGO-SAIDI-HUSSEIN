# Question 24: Polymorphism: Machine Maintenance
class Machine:
    def perform_maintenance(self):
        print("Generic machine maintenance.")
class WaterPump(Machine):
    def perform_maintenance(self):
        print("Water pump maintenance: Check impeller, lubricate bearings.")
class Generator(Machine):
    def perform_maintenance(self):
        print("Generator maintenance: Check oil level, clean air filter.")
def service_machine(machine_object):
    machine_object.perform_maintenance()
service_machine(WaterPump())
service_machine(Generator())
print("-" * 20)
