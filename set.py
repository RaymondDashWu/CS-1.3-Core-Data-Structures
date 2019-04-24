#!python

# [TODO] Add unit tests
from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
        self.hashtable = HashTable()
        # size already implemented in HashTable

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.hashtable.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set({!r})'.format(self.hashtable.items())

    # functions within the set
    def contains(self,element):
        # return a boolean indicating whether element is in this set
        return self.hashtable.contains(element)

    def add(self, element):
        # add element to this set, if not present already
        if self.contains(element) != True:
            self.hashtable.set(None, element) # key, value
        else:
            return "Element not found"

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        if self.contains(element):
            self.hashtable.delete(element)
        # Error handling done in hashtable delete function

    def union(self, other_set):
        # return a new set that is the union of this set and other_set
        pass #[TODO]

    def intersection(self, other_set):
        # return a new set that is the intersection of this set and other_set
        pass #[TODO]

    def difference(self, other_set):
        # return a new set that is the difference of this set and other_set
        pass #[TODO]
    
    def is_subset(self, other_set):
        # return a boolean indicating whether other_set is a subset of this set
        pass #[TODO]


# [TODO] Change testing function
def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()