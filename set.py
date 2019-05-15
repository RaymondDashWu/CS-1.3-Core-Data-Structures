#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
        self.hashtable = HashTable()

        if elements != None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.hashtable.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set({!r})'.format(self.hashtable.items())

    def size(self):
        return self.hashtable.size

    # functions that do stuff within the set class
    def contains(self,element):
        """Returns a boolean indicating whether element is in this set
           Time Complexity: O(L) where L is the average number of items in the bucket
           Space Complexity: O(1) does not take up any space as it just returns an element"""
        return self.hashtable.contains(element)

    def add(self, element):
        """Add element to this set, if not present already
           Time Complexity: O(L) where L is the average number of items in the bucket
           Space Complexity: O(1) does not take up any space as it just returns an element"""
        if self.contains(element) != True:
            self.hashtable.set(element, None) # key, value

    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError
           Time Complexity: O(L) where L is the average number of items in the bucket
           Space Complexity: O(1) does not take up any space as it just returns an element"""
        if self.contains(element):
            self.hashtable.delete(element)
        else:
            raise KeyError('Element be missing!')

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set
           Time Complexity: O(n) iterating through n buckets
           Space Complexity: O(n) as a new set is created - union_set"""
        union_set = Set(self.hashtable.keys())

        for element in other_set.hashtable.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set
           Time Complexity: O(n) iterating through n buckets
           Space Complexity: O(n) if bigger_set & smaller_set are pointers or O(n^3) if Python creates memory for bigger_set & smaller_set 
           TODO - Research how Python assignments work"""
        intersected_set = Set()

        # Slight optimization - determine which set is smaller
        if other_set.size() > self.size():
            bigger_set = other_set
            smaller_set = self
        else:
            bigger_set = self
            smaller_set = other_set

        for element in smaller_set.hashtable.keys():
            if bigger_set.contains(element):
                intersected_set.add(element)
        return intersected_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set
           Time Complexity: O(n) iterating through n buckets
           Space Complexity: O(n) if bigger_set & smaller_set are pointers or O(n^3) if Python creates memory for bigger_set & smaller_set 
           TODO - Research how Python assignments work"""
        # PSEUDO BRAINSTORM
        # return union - intersection
        union_set = self.union(other_set)
        intersection_set = self.intersection(other_set)

        # Slight optimization - determine which set is smaller
        # Unsure if this is needed. Presumably intersection_set is always smaller than union? Didn't think
        # of edge cases so this is left in here
        if union_set.size() > intersection_set.size():
            bigger_set = union_set
            smaller_set = intersection_set
        else:
            bigger_set = intersection_set
            smaller_set = union_set

        for element in smaller_set.hashtable.keys():
            if bigger_set.contains(element):
                bigger_set.remove(element)
        return bigger_set
        
    
    def is_subset(self, other_set):
        """Return a boolean indicating whether other_set is a subset of this set
           Time Complexity: O(n) iterating through n buckets
           Space Complexity: O(1) only one variable will ever be created - counter"""
        # Note: a subset is a set which is entirely contained within another set

        counter = 0

        for element in other_set.hashtable.keys():
            if self.contains(element):
                counter += 1
        return counter == other_set.size()