from unittest import TestCase

from array_2d import hourglass_sum

sample_input = [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]]


sample_test_case1 = [[1, 1, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0],
                     [1, 1, 1, 0, 0, 0],
                     [0, 9, 2, -4, -4, 0],
                     [0, 0, 0, -2, 0, 0],
                     [0, 0, -1, -2, -4, 0]]


sample_test_case2 = [[9, -9, -9, 1, 1, 1],
                     [0, -9, 0, 4, 3, 2],
                     [-9, -9, -9, 1, 2, 3],
                     [0, 0, 8, 6, 6, 0],
                     [0, 0, 0, -2, 0, 0],
                     [0, 0, 1, 2, 4, 0]]


class TestHourglassSum(TestCase):
    def test_sample_input(self):
        self.assertEqual(hourglass_sum(sample_input), 19)

    def test_case1(self):
        self.assertEqual(hourglass_sum(sample_test_case1), 13)

    def test_case2(self):
        self.assertEqual(hourglass_sum(sample_test_case2), 28)
