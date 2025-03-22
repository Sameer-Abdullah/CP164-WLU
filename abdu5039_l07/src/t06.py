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

array = [22, 44, 55, 55, 11]

for value in array:
    lst.append(value)

lst.reverse_r()

for value in lst:
    print(value)