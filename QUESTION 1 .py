# Question 1: Crop Yield Data Analysis
yield_data = [3.5, 4.2, 3.9, 4.5, 5.1, 4.8, 5.5, 5.3, 5.8, 6.2]

average_yield = sum(yield_data) / len(yield_data)
highest_yield = max(yield_data)
lowest_yield = min(yield_data)
above_5_tonnes = sum(1 for yield_val in yield_data if yield_val > 5.0)

print(f"Average yield: {average_yield:.2f} tonnes")
print(f"Highest yield: {highest_yield} tonnes")
print(f"Lowest yield: {lowest_yield} tonnes")
print(f"Years with yield above 5.0 tonnes: {above_5_tonnes}")
