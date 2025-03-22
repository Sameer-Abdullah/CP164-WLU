"""
-------------------------------------------------------
[Assignment 1 task 7]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import max_diff

string_values = input('Enter values (seperated by a comma): ').split(',')

values = []

for i in string_values:
    values.append(int(i))

diff = max_diff(values)

print(f"Biggest Difference: {diff}")


