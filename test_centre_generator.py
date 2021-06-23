import unittest
from centre_generator import waiting_list, centre_list, open_centre_list, full_centres, rand_centre_trainees
from centre_generator import add_trainee_to_centre


#  Testing the waiting_list variable is indeed a list.
class TestingWaitList(unittest.TestCase):
    def test_trainees(self):
        self.assertIsInstance(waiting_list, list)


#  Testing the centre_list variable is indeed a list.
class TestingCentreList(unittest.TestCase):
    def test_trainees(self):
        self.assertIsInstance(centre_list, list)


#  Testing the open_centre_list variable is indeed a list.
class TestingOpenCentreList(unittest.TestCase):
    def test_trainees(self):
        self.assertIsInstance(open_centre_list, list)


#  Testing the full_centres variable is indeed a list.
class TestingFullCentresIsList(unittest.TestCase):
    def test_trainees(self):
        self.assertIsInstance(full_centres, list)


#  Testing the random number generator for monthly trainee allocations.
class TestRandCentreGen(unittest.TestCase):

    #  Tests whether an integer is created first.
    def test_num_is_int(self):
        self.assertIsInstance(rand_centre_trainees(), int)

    #  Tests whether the integer falls between 20 and 30.
    def test_num_in_range(self):
        self.assertGreaterEqual(rand_centre_trainees(), 20)
        self.assertLessEqual(rand_centre_trainees(), 30)
