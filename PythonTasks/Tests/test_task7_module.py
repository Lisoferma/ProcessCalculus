__author__ = "Lisoferma"

import sys
import math
import unittest

sys.path += ["C:\\Users\\User\\Desktop\\PC\\PythonTasks"]

from Modules import task7_module as module


class TestTask7Module(unittest.TestCase):

    def test_calculate_sum__n_equal_0__return_0(self):
        n = 0
        expected_sum = 0

        self.assertEqual(module.calculate_sum(n), expected_sum)

    def test_calculate_sum__n_equal_1__return_1(self):
        n = 1
        expected_sum = 1

        self.assertEqual(module.calculate_sum(n), expected_sum)

    def test_calculate_sum__n_equal_2__return_expected_sum(self):
        n = 2
        expected_sum = 1.04166666667

        self.assertTrue(math.isclose(module.calculate_sum(n), expected_sum))

    def test_calculate_sum__n_equal_3__return_expected_sum(self):
        n = 3
        expected_sum = 1.0416694224

        self.assertTrue(math.isclose(module.calculate_sum(n), expected_sum))


if __name__ == '__main__':
    unittest.main()
