"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

array = [22, 44, 33, 55, 11]

for value in array:
    lst.append(value)

p, c, i = lst._linear_search_r(33)

print(p._value)
print(c._value)
print(i)