"""
-------------------------------------------------------
[Lab 3 Task 5]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.remove())