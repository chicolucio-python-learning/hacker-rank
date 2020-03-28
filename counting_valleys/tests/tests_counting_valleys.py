from unittest import TestCase

from counting_valleys import counting_valleys


class TestCountingValleys(TestCase):
    def test_description(self):
        self.assertEqual(counting_valleys(8, 'DDUUUUDD'), 1)

    def test_sample_input(self):
        self.assertEqual(counting_valleys(8, 'UDDDUDUU'), 1)

    def test_sample_test_case_1(self):
        self.assertEqual(counting_valleys(12, 'DDUUDDUDUUUD'), 2)
