import unittest
from unittest.mock import patch
from user_input import months_input


#  Testing the input of the user.
class MyTestCase(unittest.TestCase):
    #  Uses a mock input to run the test.
    def runTest(self):
        with patch('builtins.input', return_value=6):
            months_input()
            self.assertEqual(months_input(), 6)
