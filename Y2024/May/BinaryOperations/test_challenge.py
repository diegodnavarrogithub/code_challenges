import unittest

from Y2024.May.BinaryOperations.challenge import binary_operations


class TestBinaryOperations(unittest.TestCase):
    def test_binary_operations(self):

        ans = binary_operations("1C0C1C1A0B1")
        expected_ans = 1
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
