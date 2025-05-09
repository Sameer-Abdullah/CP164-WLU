"""
-------------------------------------------------------
[Assignment 8, Task 1]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-03-12"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()

arr = [3, 1, 5, 0, 2, 4, 6]

for value in arr:
    bst.insert(value)

print("The BST is valid?: ")
print(bst.is_valid())

print()
print("The BST is balanced?: ")
print(bst.is_balanced())

bst2 = BST()

for value in [11, 22, 33, 44]:
    bst2.insert(value)

print()
print("The BSTs are balanced?: ")
print(bst.is_balanced)

print()
print("Minimum value in BST: ")
print(bst.min())

print()
print("Number of nodes with 0 children: ")
print(bst.leaf_count())

print()
print("Number of nodes with 1 child: ")
print(bst.one_child_count())

print()
print("Number of nodes with 2 children: ")
print(bst.two_child_count())

print()
print("Values in order from bst: ")
print(bst.inorder())

print()
print("Values in preorder from bst: ")
print(bst.preorder())

print()
print("Values in postorder from bst: ")
print(bst.postorder())

print()
print("Values in levelorder from bst: ")
print(bst.levelorder())

print()
print("Removed Value: ")
print(bst.remove(3))

print()
print("Printing Updated BST: ")
for value in bst:
    print(value)