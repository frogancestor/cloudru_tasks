import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
from src.functions.number_functions import quickSort

class TestQuickSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_emptylist(self):
        self.assertEqual(quickSort([]), [])

    def test_oneitemlist(self):
        self.assertEqual(quickSort([10]), [10])

    def test_negativenumslist(self):
        self.assertEqual(quickSort([-7, -5, -1, -9, -8743, -10]), [-8743, -10, -9, -7, -5, -1])

    def test_intsandfloats(self):
        self.assertEqual(quickSort([28, 13.4, 821, -5, 0, 0.8, -90]), [-90, -5, 0, 0.8, 13.4, 28, 821])

if __name__ == "__main__":
    unittest.main()
