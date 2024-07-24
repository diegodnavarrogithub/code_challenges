import unittest

from Y2024.May.Atoi.challenge import Atoi


class TestAtoi(unittest.TestCase):
    def test_Atoi_42(self):
        ans = Atoi("42")
        expected_ans = 42
        self.assertEqual(ans, expected_ans)

    def test_Atoi_neg42(self):
        ans = Atoi(" -042")
        expected_ans = -42
        self.assertEqual(ans, expected_ans)

    def test_Atoi_1337(self):
        ans = Atoi("1337c0d3")
        expected_ans = 1337
        self.assertEqual(ans, expected_ans)

    def test_Atoi_words(self):
        ans = Atoi("words and 987")
        expected_ans = 0
        self.assertEqual(ans, expected_ans)

    def test_Atoi_leading0(self):
        ans = Atoi("0000987")
        expected_ans = 987
        self.assertEqual(ans, expected_ans)

    def test_Atoi_empty(self):
        ans = Atoi("")
        expected_ans = 0
        self.assertEqual(ans, expected_ans)

    def test_Atoi_empty_and_zeros(self):
        ans = Atoi("    0000000000000   ")
        expected_ans = 0
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
