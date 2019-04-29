from redact_problem import redact_words
from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class RedactTest(unittest.TestCase):

    def test_redact(self):
        word_bank = set(['A', 'B', 'C'])
        banned_words = set(['B', 'C'])
        assert word_bank.contains('A') == True
        assert word_bank.contains('B') == False
        assert word_bank.contains('C') == False
        assert word_bank.hashtable.size == 1

if __name__ == '__main__':
    unittest.main()