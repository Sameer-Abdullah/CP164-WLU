"""
-------------------------------------------------------
[Lab 1 Task 2]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["top", "middle", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)