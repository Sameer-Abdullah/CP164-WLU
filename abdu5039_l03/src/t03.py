"""
-------------------------------------------------------
[Lab 3 Task 3]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

queue = Queue()

source = [1, 2, 3]

array_to_queue(queue, source)

for _ in range(len(queue)):
    value = queue.remove()
    print(value)
    source.append(value)

array_to_queue(queue, source)

queue_to_array(queue, source)

print(source)

queue_test(source)