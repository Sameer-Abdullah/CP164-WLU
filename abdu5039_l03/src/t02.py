"""
-------------------------------------------------------
[Lab 3 Task 2]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:          169065039
Email:     abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

insert_value = input("Enter a value: ")

queue.insert(insert_value)

print(queue.peek())

value = queue.remove()

print(value)