from unittest import TestCase

from array_rotation import rot_left


class TestArrayRotation(TestCase):
    def test_description_example(self):
        self.assertEqual(rot_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])

    def test_sample_input(self):
        self.assertEqual(rot_left([1, 2, 3, 4, 5], 4), [5, 1, 2, 3, 4])

    def test_case1(self):
        self.assertEqual(rot_left(
            [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10), [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77])  # NoQA

    def test_case2(self):
        self.assertEqual(rot_left([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97], 13), [  # NoQA
                         87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60])  # NoQA
