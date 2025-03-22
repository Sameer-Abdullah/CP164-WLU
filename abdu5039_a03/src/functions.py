"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sameer Abdullah
ID:      169065039
Email:   abdu5039@mylaurier.ca
__updated__ = "2024-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

OPERATORS = "+-*/"

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target = Stack()
        
    while (not source1.is_empty()) and (not source2.is_empty()):
        target.push(source1.pop())
        target.push(source2.pop())
    # If the stacks are not equal in length
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
        
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp = []
    
    while not source.is_empty():
        temp.append(source.pop())
    while len(temp) > 0:
        source.push(temp.pop(0))
    return None

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    chars = ""
    for s in string:
        if s.isalpha():
            chars += s.lower()
            
    l = len(chars)
    mid = -1
    if l == 0:
        palindrome = True
    else:
        mid = l // 2
        first_half = Stack()
        for i in range(mid):
            first_half.push(chars[i])
        if l % 2 == 0:
            second_half_chars = chars[mid:]
        else:
            second_half_chars = chars[mid + 1:]
        second_half_chars = second_half_chars.lower()  
        i = 0
        while palindrome and i < mid:
            s = second_half_chars[i]
            p = first_half.pop()
            if s == p:
                i += 1
            else:
                palindrome = False
    return palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()
    for x in elements:
        if x not in OPERATORS:
            stack.push(x)
        else:
            first = float(stack.pop())
            second = float(stack.pop())
            if x =="+":
                stack.push(second + first)
            elif x == "-":
                stack.push(second - first)
            elif x == "*":
                stack.push(second * first)
            else:
                stack.push(second / first)
    answer = float(stack.pop())
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    try:
        current = "Start"
        choices = maze[current]
        path = []
        if "X" in choices:
            path.append("X")
        stack = Stack()
        while "X" not in choices:
            for c in choices:
                stack.push(c)
            current = stack.pop()
            if maze[current]!=[]:
                path.append(current)          
            choices = maze[current]
            if "X" in choices:
                path.append("X")
    except:     
        path = None
    finally:
        return path