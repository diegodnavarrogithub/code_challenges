import unittest

from Y2024.May.StringTransformation.challenge import string_transformation


class TestStringTransformation(unittest.TestCase):
    def test_string_transformation(self):

        ans = string_transformation()
        expected_ans = 3
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

