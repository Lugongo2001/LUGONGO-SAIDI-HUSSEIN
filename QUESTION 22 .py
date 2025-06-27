# Question 22: Overriding: Animal Feeding
class Livestock:
    def feed(self):
        print("This animal eats generic food.")
class Cow(Livestock):
    def feed(self):
        print("Cow is eating fresh grass and silage.")
class Chicken(Livestock):
    def feed(self):
        print("Chicken is pecking at grains and corn.")
animals = [Cow(), Chicken()]
for animal in animals:
    animal.feed()
print("-" * 20)
