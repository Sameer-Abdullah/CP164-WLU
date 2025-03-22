"""
-------------------------------------------------------
[Assignment 1 Task 3]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
from Food_utilities import read_foods, calories_by_origin

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

avg = calories_by_origin(foods, 2)

print(f"Average Calories: {avg}")