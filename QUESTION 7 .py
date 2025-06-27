# Question 7: Crop Nutrient Lookup
crop_nutrients = {'Maize': {'N': 120, 'P': 60, 'K': 60}, 'Rice': {'N': 100, 'P': 50, 'K': 50}}
crop_name = input("Enter crop name: ")
nutrient = input("Enter nutrient (N, P, or K): ")
try:
    print(f"Nutrient requirement for {crop_name}: {crop_nutrients[crop_name][nutrient]} kg/ha")
except KeyError:
    print("Invalid crop name or nutrient.")
