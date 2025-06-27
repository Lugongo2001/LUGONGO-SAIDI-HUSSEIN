# Question 3: Weekly Rainfall Analysis
rainfall = [10.2, 0.0, 5.5, 1.2, 8.0, 0.0, 3.5]
total_rainfall = sum(rainfall)
no_rainfall_days = [f"Day {i+1}" for i, rainfall_val in enumerate(rainfall) if rainfall_val == 0.0]

print(f"Total weekly rainfall: {total_rainfall:.1f} mm")
print(f"Days with no rainfall: {', '.join(no_rainfall_days)}")
