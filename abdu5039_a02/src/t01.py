"""
-------------------------------------------------------
[Assignment 1 Task 1]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods, by_origin

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")