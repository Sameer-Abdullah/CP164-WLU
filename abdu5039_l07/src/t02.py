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

lst1 = List()

lst2 = List()

array = [22, 44, 33, 55, 11]

array2 = [22, 44, 11, 55, 11]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

print(lst1.is_identical_r(lst2))