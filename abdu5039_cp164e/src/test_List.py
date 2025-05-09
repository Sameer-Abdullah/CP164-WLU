"""
-------------------------------------------------------
Exam: Simple List testing
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@wlu.ca
__updated__ = "2024-04-23"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
VALUES = [3, 8, 6, 7, 7, 6, 2, 2, 2, 4, 12]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_List(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_split_count():
    """
    Tests the 'split_count' method.
    """
    print(SEP)
    print("Test 'split_count'")
    print()

    source = to_List(VALUES)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_count(0)
    print("target1, target2 = source.split_count(0)")
    print(f"  target1: {to_python_list(target1)}")
    print(f"  target2: {to_python_list(target2)}")
    print(f"  source: {to_python_list(source)}")
    print()
    print()

    source = to_List(VALUES)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_count(99)
    print("target1, target2 = source.split_count(99)")
    print(f"  target1: {to_python_list(target1)}")
    print(f"  target2: {to_python_list(target2)}")
    print(f"  source: {to_python_list(source)}")
    print()
    print()

    source = to_List(VALUES)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_count(5)
    print("target1, target2 = source.split_count(5)")
    print(f"  target1: {to_python_list(target1)}")
    print(f"  target2: {to_python_list(target2)}")
    print(f"  source: {to_python_list(source)}")
    print()
    print()


def test_replace_many():
    """
    Tests the 'replace_many' method.
    """
    print(SEP)
    print("Test 'replace_many'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.replace_many(9, -1)
    print(f"  After 'replace_many(9, -1)': {to_python_list(source)}")
    print()

    source = to_List([9]*6)
    print(f"  List: {to_python_list(source)}")
    source.replace_many(9, 8)
    print(f"  After 'replace_many(9, 8)': {to_python_list(source)}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.replace_many(6, 0)
    print(f"  After 'replace_many(6, 0)': {to_python_list(source)}")
    print()


def test_rotate_rear():
    """
    Tests the 'rotate_rear' method.
    """
    print(SEP)
    print("Test 'rotate_rear'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()

    source = to_List(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()


def test_has_loop():
    """
    Tests the 'has_loop' method.
    """
    print(SEP)
    print("Test 'has_loop'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.has_loop()}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._rear._next = source._rear")
    source._rear._next = source._rear
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._front._next._next._next = source._front._next")
    source._front._next._next._next = source._front._next
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._front._next = source._front")
    source._front._next = source._front
    print(f"  Has Loop: {source.has_loop()}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    test_split_count()
    test_replace_many()
    test_rotate_rear()
    test_has_loop()
