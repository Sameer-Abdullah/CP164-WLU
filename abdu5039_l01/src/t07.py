"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, get_vegetarian
# Constants

with open("foods.txt", "r") as f:
    foods = read_foods(f)

veggies = get_vegetarian(foods)

print("Vegetarian Foods:")
for food in veggies:
    print(food.name)