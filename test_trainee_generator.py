import unittest
from trainee_generator import rand_new_trainees, waiting_list


#  Testing the random number generator for monthly trainee intake.
class TestRandGen(unittest.TestCase):

    #  Tests whether an integer is created first.
    def test_num_is_int(self):
        self.assertIsInstance(rand_new_trainees(), int)

    #  Tests whether the integer falls between 20 and 30.
    def test_num_in_range(self):
        self.assertGreaterEqual(rand_new_trainees(), 20)
        self.assertLessEqual(rand_new_trainees(), 30)


#  Testing that the waiting_list output is actually a list
class ListTests(unittest.TestCase):
    def test_trainees(self):
        self.assertIsInstance(waiting_list, list)
