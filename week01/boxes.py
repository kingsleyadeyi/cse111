"""
A manufacturing company needs a program that helps employees
determine how many boxes are needed to pack manufactured items.
"""

import math

# Ask the user for input
items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed
boxes_needed = math.ceil(items / items_per_box)

# Display the result
print(
    f"For {items} items, packing {items_per_box} items in each box, "
    f"you will need {boxes_needed} boxes."
)