"""
-------------------------------------------------------
[Assignment 1 Task 3]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse

stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

stack_reverse(stack)

for i in stack:
    print(i)