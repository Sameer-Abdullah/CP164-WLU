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
from Food_utilities import write_foods
from Food import Food
fv = open("new_foods.txt", "w")

k = Food("Milk", 2, False, 130)
y = Food("Sandwich", 0, True, 500)

l = [k, y]
write_foods(fv, l)
fv.close()