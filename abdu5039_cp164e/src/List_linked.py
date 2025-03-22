"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Sameer Abdullah
ID:     169065039
Email:  abdu5039@mylaurier.ca
__updated__ = "2024-04-23"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy
from pickle import NONE


class List:
    """
    A linked List class.
    """

    def split_count(self, count):
        """
        -------------------------------------------------------
        Splits source into separate target lists based on count.
        At finish target1 contains count nodes, target2 contains 
        remaining nodes from source, and source is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_count(count)
        -------------------------------------------------------
        Parameters:
            count - the number of nodes in target1 (int >= 0)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            target1 - contains count nodes from source (List)
            target2 - contains remaining nodes from source (List)
        -------------------------------------------------------
        """
        # This will create new lists to store split parts
        target1 = List()
        target2 = List()
    
        # if the count == 0, it will move all nodes to traget2 and clear all the sources.
        if count == 0:
            target2._front = self._front
            target2._rear = self._rear
            self._front = None
            self._rear = None
        else:
            # This will start it from the font of the list
            current = self._front
            previous = None
            i = 0
            # This will iterate through the list until count nodes are passed or the list ends.
            while current is not None and i < count:
                previous = current
                current = current._next
                i += 1
    
            if previous is not None:
                previous._next = None
    
            target1._front = self._front
            target1._rear = previous
            
            # this will reset the sources front to the remiander of the list
            self._front = current
    
            # If there is no remainder, it will set target2 to empty
            if current is None:
                target2._front = None
                target2._rear = None
            else:
                target2._front = current
                target2._rear = self._rear
                self._rear = None
    
        # This will return the two new lists. 
        return target1, target2

    def replace_many(self, key, value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in source with value.
        List is otherwise unchanged.
        Use: source.replace_many(key, value)
        -------------------------------------------------------
        Parameters:
            key - a key that may be in source (?)
            value - the replacement for key (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            None.
        -------------------------------------------------------
        """
        # This will initlialize current to point to the very first node in the list
        current = self._front
        
        # This will loop until current is None, which is the end of the list
        while current is not None:
            # This will check if the current node's value is key and then it will replace it with value
            if current._value == key:
                # This will shift the node in the list 
                current._value = value
            current = current._next
        # This will return NONE
        return None              
    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            None
        -------------------------------------------------------
        """
        # this will check if there is more then one node in the list 
        if self._front is not None and self._rear is not None and self._front != self._rear:
            # this will start by finding the node just before the rear node
            current = self._front
            while current._next != self._rear:
                current = current._next
    
            # this will move the rear node to the front of the list
            self._rear._next = self._front  
            # this wil update the front to be the rear
            self._front = self._rear  
            self._rear = current
            # this will set the new rear's next to None, severing the link
            self._rear._next = None  
        return None

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """
        if self._front is None:
            loop = False
    
        slow_ptr = self._front
        fast_ptr = self._front
    
        while fast_ptr is not None and fast_ptr._next is not None:
            # Moves one step
            slow_ptr = slow_ptr._next  
            # Moves two steps        
            fast_ptr = fast_ptr._next._next    
    
            if slow_ptr == fast_ptr:
                # A loop is found if both pointers meet
                loop = True  
    
        # No loop found if the while loop exits normally
        loop = False 
        # this will return  loop
        return loop 
    
# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​‌​​‌​​‌‌‌‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
