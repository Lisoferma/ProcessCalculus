__author__ = "Lisoferma"

import unittest
from Modules import task5_module as module


class TestTask5Module(unittest.TestCase):

    def test_calculate_sum__data_is_filled__return_expected_sum(self):
        data = [1, 2, 3, 4, 5]
        expected_sum = 4.375

        self.assertEqual(module.calculate_sum(data), expected_sum)

    def test_calculate_sum__data_is_one_item__return_zero(self):
        data = [5]
        expected_sum = 0

        self.assertEqual(module.calculate_sum(data), expected_sum)

    def test_calculate_sum__data_is_empty__return_zero(self):
        data = []
        expected_sum = 0

        self.assertEqual(module.calculate_sum(data), expected_sum)


if __name__ == '__main__':
    unittest.main()
