import unittest

from Y2024.May.FirstUniqueCharacter.challenge import first_unique_character


class TestFirstUniqueCharacter(unittest.TestCase):
    def test_first_unique_character_0(self):
        ans = first_unique_character("leetcode")
        expected_ans = 0
        self.assertEqual(ans, expected_ans)

    def test_first_unique_character_2(self):
        ans = first_unique_character("loveleetcode")
        expected_ans = 2
        self.assertEqual(ans, expected_ans)

    def test_first_unique_character_no_uniques(self):
        ans = first_unique_character("aabb")
        expected_ans = -1
        self.assertEqual(ans, expected_ans)

    def test_first_unique_character_last_index(self):
        ans = first_unique_character("dddccdbba")
        expected_ans = 8
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
