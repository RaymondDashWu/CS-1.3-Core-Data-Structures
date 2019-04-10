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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Time - O(log(n)) Space - O(1)
    # TODO: Annotate functions with complexity analysis of running time and space (memory)
    
    # PSEUDO BRAINSTORM 2
    # check if item at middle of array is equal to item
    # if not, compare whether or not the item is greater or equal to middle item
    # if greater, repeat for half in the range of middle item to end
    # if less, repeat for half in the range of beginning to middle item
    array.sort()
    middle = len(array) // 2

    while array[middle] != item:
        if array[middle] > item:
            array = range(array[middle], array[-1])
        elif array[middle] < item:
            array = range(0, array[middle])
        elif array[middle] == item:
            return middle

    # if array[middle] == item:
    #     return middle
    # else:
    #     if array[middle] > item:
    #         new_array = range(array[middle], )


    
    
    
    
    
    
    
    
    # for index, value in enumerate(array):
    #     if item == value:
    #         return index
    #     else:
    #         if value > len(array)/2:
    #             return index[]
            # PSEUDO BRAINSTORM
            # turn to decimal and compare greater or less than
            # keep track of length of array
            # change index to index range
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # TODO: Annotate functions with complexity analysis of running time and space (memory)
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests