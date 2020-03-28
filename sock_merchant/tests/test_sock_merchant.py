from unittest import TestCase

from sock_merchant import sock_merchant

# Tests based on input and output samples from the problem description


class TestSockMerchant(TestCase):
    def test_description(self):
        self.assertEqual(sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)

    def test_sample_input(self):
        self.assertEqual(sock_merchant(
            9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)

    def test_sample_test_case_1(self):
        self.assertEqual(sock_merchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]), 4)
