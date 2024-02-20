__author__ = "Lisoferma"

import unittest
from Modules import task6_module as module


class TestTask6Module(unittest.TestCase):

    def test_count_multiple_3_not_5__data_for_all_conditions__return_expected_count(self):
        data = [1, 2, 3, 4, 5, 6, 15, 300]
        expected_count = 2

        self.assertEqual(module.count_multiple_3_not_5(data), expected_count)

    def test_count_multiple_3_not_5__data_not_satisfy_any_condition__return_zero(self):
        data = [1, 2, 4, 5, 15, 300]
        expected_count = 0

        self.assertEqual(module.count_multiple_3_not_5(data), expected_count)

    def test_count_multiple_3_not_5__data_is_empty__return_zero(self):
        data = []
        expected_count = 0

        self.assertEqual(module.count_multiple_3_not_5(data), expected_count)


if __name__ == '__main__':
    unittest.main()
