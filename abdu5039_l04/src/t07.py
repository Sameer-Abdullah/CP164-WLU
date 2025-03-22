"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-29"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test

file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)