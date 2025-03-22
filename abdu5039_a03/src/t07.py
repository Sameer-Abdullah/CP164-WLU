"""
-------------------------------------------------------
[Assignment 1 Task 7  ]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
from functions import stack_maze
def main():
    maze = {'Start': ['A'], 'A':['C', 'B'], 
            'B':[], 'C':['D', 'X']}
    path = stack_maze(maze)
    print(path)
main()