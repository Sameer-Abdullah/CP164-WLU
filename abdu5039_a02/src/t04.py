"""
-------------------------------------------------------
[Assignment 1 Task 4]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, food_table

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

food_table(foods)