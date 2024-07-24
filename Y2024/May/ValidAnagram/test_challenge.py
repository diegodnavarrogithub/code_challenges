import unittest

from Y2024.May.ValidAnagram.challenge import valid_anagram


class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        s = "anagram"
        t = "nagaram"
        ans = valid_anagram(s, t)
        expected_ans = True
        self.assertEqual(ans, expected_ans)

    def test_invalid_anagram(self):
        s = "rat"
        t = "car"
        ans = valid_anagram(s, t)
        expected_ans = False
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":

    unittest.main()
