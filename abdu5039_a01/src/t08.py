"""
-------------------------------------------------------
[Assignment 1 task 8]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""

from functions import matrix_stats

a = [[1, 2, 3], [100, -99, 10]]
print(a)

small, large, total, average = matrix_stats(a)

print(f'Smallest Value: {small}')
print(f"Largest Value: {large}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")