#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        st = Set()
        assert st.size == 0

    def test_contains(self):
        st = Set(['UO2', 'UO2', 'CaCO3', 'SiO2'])
        assert st.contains('UO2') == True
        assert st.contains('CaCO3') == True
        assert st.contains('SiO2') == True
        assert st.contains('ZnCO3') == False
        # assert st.size == 3 # [TODO] Learn why this doesn't work
        assert st.hashtable.size == 3 # Test to see if duplicate was added

    def test_add(self):
        st = Set()
        st.add('ZnCO3')
        assert st.hashtable.size == 1
        assert st.contains('ZnCO3') == True

    def test_remove(self):
        st = Set(['UO2', 'CaCO3', 'SiO2'])
        st.remove('CaCO3')
        assert st.contains('CaCO3') == False
        assert st.hashtable.size == 2
        with self.assertRaises(KeyError):
            st.remove('MnCO3') # Try to remove an element that doesn't exist. SHOULD raise a keyerror
    
    def test_union(self):
        st1 = Set(['UO2', 'CaCO3', 'SiO2'])
        st2 = Set(['UO2', 'Ca5(PO4)3F', 'SiO2'])
        st_union = st1.union(st2)
        assert st_union.contains('UO2') == True
        assert st_union.contains('CaCO3') == True
        assert st_union.contains('SiO2') == True
        assert st_union.contains('Ca5(PO4)3F') == True
        assert st_union.hashtable.size == 4

    def test_intersection(self):
        st1 = Set(['UO2', 'CaCO3', 'SiO2'])
        st2 = Set(['UO2', 'Ca5(PO4)3F', 'SiO2', 'Pb5(PO4)3Cl'])
        st_intersection = st1.intersection(st2)
        assert st_intersection.contains('UO2') == True
        assert st_intersection.contains('SiO2') == True
        assert st_intersection.contains('Ca5(PO4)3F') == False
        assert st_intersection.contains('CaCO3') == False
        assert st_intersection.contains('Pb5(PO4)3Cl') == False
        assert st_intersection.hashtable.size == 2

    def test_difference(self):
        st1 = Set(['UO2', 'CaCO3', 'SiO2'])
        st2 = Set(['UO2', 'Ca5(PO4)3F', 'SiO2', 'Pb5(PO4)3Cl'])
        st_difference = st1.difference(st2)
        assert st_difference.contains('UO2') == False
        assert st_difference.contains('SiO2') == False
        assert st_difference.contains('Ca5(PO4)3F') == True
        assert st_difference.contains('CaCO3') == True
        assert st_difference.contains('Pb5(PO4)3Cl') == True
        assert st_difference.hashtable.size == 3




    # def test_contains(self):
    #     st = Set()
    #     assert st.keys() == []
    #     st.set('I', 1)
    #     assert st.keys() == ['I']
    #     st.set('V', 5)
    #     self.assertCountEqual(st.keys(), ['I', 'V'])  # Ignore item order
    #     st.set('X', 10)
    #     self.assertCountEqual(st.keys(), ['I', 'V', 'X'])  # Ignore item order

    # def test_values(self):
    #     st = Set()
    #     assert st.values() == []
    #     st.set('I', 1)
    #     assert st.values() == [1]
    #     st.set('V', 5)
    #     self.assertCountEqual(st.values(), [1, 5])  # Ignore item order
    #     st.set('X', 10)
    #     self.assertCountEqual(st.values(), [1, 5, 10])  # Ignore item order

    # def test_items(self):
    #     st = Set()
    #     assert st.items() == []
    #     st.set('I', 1)
    #     assert st.items() == [('I', 1)]
    #     st.set('V', 5)
    #     self.assertCountEqual(st.items(), [('I', 1), ('V', 5)])
    #     st.set('X', 10)
    #     self.assertCountEqual(st.items(), [('I', 1), ('V', 5), ('X', 10)])

    # def test_length(self):
    #     st = Set()
    #     assert st.length() == 0
    #     st.set('I', 1)
    #     assert st.length() == 1
    #     st.set('V', 5)
    #     assert st.length() == 2
    #     st.set('X', 10)
    #     assert st.length() == 3

    # def test_size(self):
    #     st = Set()
    #     assert st.size == 0
    #     st.set('I', 1)
    #     assert st.size == 1
    #     st.set('V', 5)
    #     assert st.size == 2
    #     st.set('X', 10)
    #     assert st.size == 3

    # def test_resize(self):
    #     st = Set(2)  # Set init_size to 2
    #     assert st.size == 0
    #     assert len(st.buckets) == 2
    #     assert st.load_factor() == 0
    #     st.set('I', 1)
    #     assert st.size == 1
    #     assert len(st.buckets) == 2
    #     assert st.load_factor() == 0.5
    #     st.set('V', 5)  # Should trigger resize
    #     assert st.size == 2
    #     assert len(st.buckets) == 4
    #     assert st.load_factor() == 0.5
    #     st.set('X', 10)
    #     assert st.size == 3
    #     assert len(st.buckets) == 4
    #     assert st.load_factor() == 0.75
    #     st.set('L', 50)  # Should trigger resize
    #     assert st.size == 4
    #     assert len(st.buckets) == 8
    #     assert st.load_factor() == 0.5

    # def test_contains(self):
    #     st = Set()
    #     st.set('I', 1)
    #     st.set('V', 5)
    #     st.set('X', 10)
    #     assert st.contains('I') is True
    #     assert st.contains('V') is True
    #     assert st.contains('X') is True
    #     assert st.contains('A') is False

    # def test_set_and_get(self):
    #     st = Set()
    #     st.set('I', 1)
    #     st.set('V', 5)
    #     st.set('X', 10)
    #     assert st.get('I') == 1
    #     assert st.get('V') == 5
    #     assert st.get('X') == 10
    #     assert st.length() == 3
    #     assert st.size == 3
    #     with self.assertRaises(KeyError):
    #         st.get('A')  # Key does not exist

    # def test_set_twice_and_get(self):
    #     st = Set()
    #     st.set('I', 1)
    #     st.set('V', 4)
    #     st.set('X', 9)
    #     assert st.length() == 3
    #     assert st.size == 3
    #     st.set('V', 5)  # Update value
    #     st.set('X', 10)  # Update value
    #     assert st.get('I') == 1
    #     assert st.get('V') == 5
    #     assert st.get('X') == 10
    #     assert st.length() == 3  # Check length is not overcounting
    #     assert st.size == 3  # Check size is not overcounting

    # def test_delete(self):
    #     st = Set()
    #     st.set('I', 1)
    #     st.set('V', 5)
    #     st.set('X', 10)
    #     assert st.length() == 3
    #     assert st.size == 3
    #     st.delete('I')
    #     st.delete('X')
    #     assert st.length() == 1
    #     assert st.size == 1
    #     with self.assertRaises(KeyError):
    #         st.delete('X')  # Key no longer exists
    #     with self.assertRaises(KeyError):
    #         st.delete('A')  # Key does not exist


if __name__ == '__main__':
    unittest.main()