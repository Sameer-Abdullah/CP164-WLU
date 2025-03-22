"""
-------------------------------------------------------
[Lab 3 Task 1]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
# Constants
from Queue_array import Queue

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))