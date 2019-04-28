#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
        self.hashtable = HashTable() # Should this be []?
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
        else:
            return "Element be missing!"

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        if self.contains(element):
            self.hashtable.delete(element)
        else:
            raise KeyError('Element be missing!')
        # Error handling done in hashtable delete function

    def union(self, other_set):
        # return a new set that is the union of this set and other_set
        union_set = Set(self.hashtable.keys())

        for element in other_set.hashtable.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        # return a new set that is the intersection of this set and other_set
        intersected_set = Set()

        other_set_copy = other_set.copy.deepcopy()

        # need to make other_set copy so that other_set element isn't deleted
        for element in intersected_set.hashtable.keys():
            if self.contains(element):
                intersected_set.add(element)
        # TODO - compare sizes of the sets. Smaller goes into bigger to go through fewer elements

        for element in other_set.hashtable.keys():
            if first_set.contains(other_set[element]):
                intersected_set.add(element)
        return intersected_set

    def difference(self, other_set):
        # return a new set that is the difference of this set and other_set
        first_set = Set(self.hashtable.values())
        difference_set = Set()

        for element in other_set:
            if first_set.contains(other_set[element]):
                first_set.remove(element)
        return difference_set
    
    def is_subset(self, other_set):
        # return a boolean indicating whether other_set is a subset of this set
        pass #[TODO]