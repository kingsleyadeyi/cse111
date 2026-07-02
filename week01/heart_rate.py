"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Ask the user for their age
age = int(input("Please enter your age: "))

# Calculate the maximum heart rate
maximum_heart_rate = 220 - age

# Calculate the target heart rate range
slowest_rate = round(maximum_heart_rate * 0.65)
fastest_rate = round(maximum_heart_rate * 0.85)

# Display the results
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest_rate} and {fastest_rate} beats per minute.")