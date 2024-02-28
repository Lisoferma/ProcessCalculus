__author__ = "Lisoferma"

import os
import sys
import numpy as np
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modules import task8_module as module


class TestTask8Module(unittest.TestCase):

    def test_get_b_array__init_array_is_filled__result_array_is_correct(self):
        init = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

        expected = np.array([[12, 27, 45],
                             [11, 24, 39],
                             [7, 15, 24]])

        result = np.zeros((3, 3), dtype=float)

        module.get_b_array(init, result)

        self.assertTrue(np.array_equal(expected, result))

    def test_get_b_array__array_size_zero__raise_exception(self):
        init = np.zeros((0, 0), float)
        result = np.zeros((0, 0), float)

        self.assertRaises(Exception, module.get_b_array, init, result)


if __name__ == '__main__':
    unittest.main()
