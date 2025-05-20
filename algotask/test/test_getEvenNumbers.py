import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from src.functions.number_functions import getEvenNumbers

class TestGetEvenNunbers(unittest.TestCase):

    def setUp(self):
        pass

    def test_emptylist(self):
        self.assertEqual(getEvenNumbers([]), [])

    def test_onlyfloat(self):
        self.assertEqual(getEvenNumbers([0.2, 88736.6254, 0.0, 1.6, 7.5, -98775.54]), [])

    def test_onlyint(self):
        self.assertEqual(getEvenNumbers([1, 296, -942, 0, 6, 8, -7]), [296, -942, 0, 6, 8])

if __name__ == "__main__":
    unittest.main()
