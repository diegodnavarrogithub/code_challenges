import unittest

from Y2024.May.SecondLargest.challenge import second_largest


class TestSecondLargest(unittest.TestCase):
    def test_second_largest(self):
        nums =  [5, 6, 8, 4, 33, 7]
        ans = second_largest(nums)
        expected_ans = 8
        self.assertEqual(ans, expected_ans)

if __name__ == '__main__':
    unittest.main()

