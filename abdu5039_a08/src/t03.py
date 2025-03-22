"""
-------------------------------------------------------
[Assignment 8, Task 3]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-03-12"
-------------------------------------------------------
"""
# Imports

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('miserables.txt', 'rt')

do_comparisons(file, bst)

file.close()

letter_table(bst)