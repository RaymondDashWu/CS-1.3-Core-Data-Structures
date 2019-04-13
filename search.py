#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: Annotate functions with complexity analysis of running time and space (memory)
    # Time - O(1) Space - O(1)
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    array.sort()
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Time - O(log(n)) Space - O(1)
    
    # PSEUDO BRAINSTORM 2
    # check if item at middle of array is equal to item
    # if not, compare whether or not the item is greater or equal to middle item
    # if greater, repeat for half in the range of middle item to end
    # if less, repeat for half in the range of beginning to middle item
    
    middle = len(array) // 2
    left = 0
    right = len(array) - 1
    
    # Logic: Look for an item by starting out with the middle of each array and then updating the range
    # so that it looks in the middle every time.

    # Ex: Looking for the name Brian in sorted list below:
    # ["Alex", "Brian", "Julia", "Kojin", "Nabil", "Nick", "Winnie"]
    # Middle (currently at array[3]) will point to "Kojin" and start to look to the left after comparing.
    # In this case the following will be looked at:
    # ["Alex", "Brian", "Julia", ...]
    # right = middle (currently 2) - 1
    # left = 0 (unchanged)
    # Brian found!
    while array[middle] != item:
        # Covers edge cases where searches go out of bounds on either left or right side
        if middle == right or left > (len(array) - 1):
            return None
        # Right looking. If item is on the right side after middle lookup
        if array[middle] < item:
            left = middle + 1
            middle = (right - left) // 2 + left
        # Left looking. If the item is on the left side after middle lookup
        elif array[middle] > item:
            right = middle - 1
            middle = (right - left) // 2
    return middle


def binary_search_recursive(array, item, left=0, right=None):
    # Time - O(log(n)) Space - O(1)
    # Set to None because only want it to run once
    if right == None:
        right = len(array) - 1
    middle = (left + right) // 2

    # Logic: see above for logic & pseudocode
    if array[middle] == item:
        return middle
    while array[middle] != item:
        # Covers edge cases where searches go out of bounds on either left or right side
        if middle == left or left > (len(array) - 1):
            return None
        # Right looking. If item is on the right side after middle lookup
        elif array[middle] < item:
            return binary_search_recursive(array, item, middle + 1, right)
        # Left looking. If the item is on the left side after middle lookup
        elif array[middle] > item:
            return binary_search_recursive(array, item, left, middle - 1)
    