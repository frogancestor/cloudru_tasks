import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from src.functions.number_functions import getMax

class TestGetMax(unittest.TestCase):

    def setUp(self):
        pass

    def test_emptylist(self):
        with self.assertRaises(ValueError) as e:
            getMax([])
        self.assertEqual('Empty list error', e.exception.args[0])

    def test_list(self):
        self.assertEqual(getMax([12, -826, 60, 188, 38, 49, 65]), 188)

    def test_equals(self):
        self.assertEqual(getMax([6, 6, 6, 6, 6, 6, 6]), 6)

if __name__ == "__main__":
    unittest.main()
