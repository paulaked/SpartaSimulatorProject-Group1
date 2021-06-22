import unittest
from user_input import months_input

class TestUserInput(unittest.TestCase):
    def test_num_is_int(self):
        self.assertIsInstance(months_input(), int)

