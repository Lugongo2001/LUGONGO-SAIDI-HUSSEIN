# Question 27: Data Management: Dictionaries and Classes
class Tractor:
    def __init__(self, registration, horsepower):
        self.registration = registration
        self.horsepower = horsepower
def display_tractor_info(tractors, plate_number):
    try:
        tractor = tractors[plate_number]
        print(f"Tractor {plate_number} horsepower: {tractor.horsepower}")
    except KeyError:
        print(f"Tractor {plate_number} not found.")
tractors = {'T 123 SUA': Tractor('T 123 SUA', 100),'T 456 SUA': Tractor('T 456 SUA', 80)}
display_tractor_info(tractors, 'T 123 SUA')
display_tractor_info(tractors, 'T 789 SUA')
print("-" * 20)
