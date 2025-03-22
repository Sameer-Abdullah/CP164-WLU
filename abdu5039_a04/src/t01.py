"""
-------------------------------------------------------
[Assignment 1 task 1]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue


target = Queue()
target.insert(1)
target.insert(2)
target.remove()

source = Queue()
source.insert(2)


equals = source == target 

print(equals)