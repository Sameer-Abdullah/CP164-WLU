"""
-------------------------------------------------------
[Assignment 1 task 5]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

source.insert(1)

source.insert(2)

source.insert(3)

key = 2

target1, target2 = pq_split_key(source, key)


print("Printing Target 1...")
while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")
while len(target2) > 0:
    print(target2.remove())