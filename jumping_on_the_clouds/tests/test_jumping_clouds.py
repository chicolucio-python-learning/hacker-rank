from unittest import TestCase

from jumping_clouds import jumping_clouds


class TestJumpingClouds(TestCase):
    def test_description(self):
        self.assertEqual(jumping_clouds([0, 1, 0, 0, 0, 1, 0]), 3)

    def test_sample_input(self):
        self.assertEqual(jumping_clouds([0, 0, 1, 0, 0, 1, 0]), 4)
