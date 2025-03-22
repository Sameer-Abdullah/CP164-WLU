"""
-------------------------------------------------------
[Lab 1 Task 3]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["First","top", "middle", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)