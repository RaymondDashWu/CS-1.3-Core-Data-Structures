#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        st = Set()
        assert st.size() == 0

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

    def test_subset(self):
        st1 = Set(['UO2', 'SiO2'])
        st2 = Set(['UO2', 'Ca5(PO4)3F', 'SiO2', 'Pb5(PO4)3Cl'])
        assert st2.is_subset(st1) == True
        assert st1.is_subset(st2) == False

if __name__ == '__main__':
    unittest.main()