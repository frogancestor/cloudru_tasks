import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from src.functions.number_functions import getMin

class TestGetMin(unittest.TestCase):

    def setUp(self):
        pass

    def test_emptylist(self):
        with self.assertRaises(ValueError) as e:
            getMin([])
        self.assertEqual('Empty list error', e.exception.args[0])

    def test_list(self):
        self.assertEqual(getMin([1092, 0, 17, -5, 900000, -78, 85]), -78)

    def test_equals(self):
        self.assertEqual(getMin([1, 1, 1, 1, 1, 1, 1]), 1)

if __name__ == "__main__":
    unittest.main()
