"""
-------------------------------------------------------
[Assignment 1 task 1]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
from functions import clean_list

n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
values = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]

clean_list(values)
