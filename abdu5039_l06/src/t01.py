"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-02-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from List_linked import List

file_variable = open("food.txts", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

new_list.append(foods[2])

new_list.prepend(foods[0])

new_list.insert(1, foods[1])

for value in new_list:
    print(value)
    print()