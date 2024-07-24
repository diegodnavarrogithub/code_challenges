import unittest

from Y2024.May.LongestCommonPrefix.challenge import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix_fl(self):
        strs = ["flower", "flow", "flight"]
        ans = longest_common_prefix(strs)
        expected_ans = "fl"
        self.assertEqual(ans, expected_ans)

    def test_longest_common_prefix_empty_res(self):
        strs = ["dog", "racecar", "car"]
        ans = longest_common_prefix(strs)
        expected_ans = ""
        self.assertEqual(ans, expected_ans)

    def test_longest_common_prefix_one_word(self):
        strs = ["a"]
        ans = longest_common_prefix(strs)
        expected_ans = "a"
        self.assertEqual(ans, expected_ans)

    def test_longest_common_prefix_2_words(self):
        strs = ["ab", "a"]
        ans = longest_common_prefix(strs)
        expected_ans = "a"
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
