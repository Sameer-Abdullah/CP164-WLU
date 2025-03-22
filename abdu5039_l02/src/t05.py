"""
-------------------------------------------------------
[Lab 1 Task 5]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import stack_test

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)