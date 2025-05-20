import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.functions.convert_functions import handleUserInput

class TestValidateUserInput(unittest.TestCase):

    def setUp(self):
        pass

    def test_wronghandleinput(self):
        with self.assertRaises(ValueError) as e:
            handleUserInput('1927 4.7 -36 739 g h')
        self.assertEqual("invalid literal for int() with base 10: 'g'", e.exception.args[0])

    def test_righthandleinput(self):
        self.assertEqual(handleUserInput('857 0 9.4 27 -2863 7'), [857, 0, 9.4, 27, -2863, 7])
        
if __name__ == "__main__":
    unittest.main()