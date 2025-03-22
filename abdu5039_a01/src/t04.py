"""
-------------------------------------------------------
[Assignment 1 task 4]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

file = open('test_file.txt', 'rt')

u, l, d, w, r = file_analyze(file)

file.close()

print(f"Uppercase Letters:    {u:>2}")
print(f"Lowercase Letters:    {l:>2}")
print(f"Digits:               {d:>2}")
print(f"Whitespace Characters:{w:>2}")
print(f"Remaining Characters: {r:>2}")