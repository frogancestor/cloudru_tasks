import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.functions.validate_functions import validateUserInput

class TestValidateUserInput(unittest.TestCase):

    def setUp(self):
        pass

    def test_inputwithchar(self):
        self.assertEqual(validateUserInput('1927 4.7 -36 739 g h'), False)

    def test_rightinput(self):
        self.assertEqual(validateUserInput('187 5 0 -9 86517 -624 0'), True)

if __name__ == "__main__":
    unittest.main()