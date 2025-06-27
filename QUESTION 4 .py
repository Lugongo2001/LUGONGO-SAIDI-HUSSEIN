
#Question 4: Soil pH Analysis with NumPy
import numpy as np
ph_values = np.array([6.2, 6.5, 5.8, 7.1, 6.0, 5.5, 6.8, 6.3, 5.9, 6.6])
# 1. Find the average pH
average_ph = np.mean(ph_values)
print(f"Average pH: {average_ph:.2f}")
# 2. Count the number of locations with acidic soil (pH < 6.0)
acidic_count = np.sum(ph_values < 6.0)
print(f"Number of acidic locations: {acidic_count}")
# 3. Categorize pH values
categories = np.where(ph_values < 6.0, 'Acidic',
                      np.where(ph_values < 7.0, 'Neutral', 'Alkaline'))
print("pH categories:", categories)
