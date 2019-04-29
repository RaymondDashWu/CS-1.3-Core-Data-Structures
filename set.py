#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
        self.hashtable = HashTable()
        self.size = self.hashtable.size

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

    # functions that do stuff within the set class
    def contains(self,element):
        # return a boolean indicating whether element is in this set
        return self.hashtable.contains(element)

    def add(self, element):
        # add element to this set, if not present already
        if self.contains(element) != True:
            self.hashtable.set(element, None) # key, value

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        if self.contains(element):
            self.hashtable.delete(element)
        else:
            raise KeyError('Element be missing!')

    def union(self, other_set):
        # return a new set that is the union of this set and other_set
        union_set = Set(self.hashtable.keys())

        for element in other_set.hashtable.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        # return a new set that is the intersection of this set and other_set
        intersected_set = Set()

        # Slight optimization - determine which set is smaller
        if other_set.hashtable.size > self.hashtable.size:
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
        # return a new set that is the difference of this set and other_set
        # PSEUDO BRAINSTORM
        # return union - intersection
        union_set = self.union(other_set)
        intersection_set = self.intersection(other_set)

        # Slight optimization - determine which set is smaller
        # Unsure if this is needed. Presumably intersection_set is always smaller than union? Didn't think
        # of edge cases so this is left in here
        if union_set.hashtable.size > intersection_set.size:
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
        # return a boolean indicating whether other_set is a subset of this set
        pass #[TODO]