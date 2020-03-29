from unittest import TestCase

from repeated_string import repeated_string


class TestRepeatedString(TestCase):
    def test_description(self):
        self.assertEqual(repeated_string('abcac', 10), 4)

    def test_sample_input0(self):
        self.assertEqual(repeated_string('aba', 10), 7)

    def test_sample_input1(self):
        self.assertEqual(repeated_string('a', 1000000000000), 1000000000000)

    def test_case7(self):
        self.assertEqual(repeated_string(
            'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 736778906400), 51574523448)  # NoQA
