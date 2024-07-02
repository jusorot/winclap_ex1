import unittest
from anagrams import anagrams


class TestAnagrams(unittest.TestCase):
    def test_train(self):
        result = anagrams("train")
        expected = ['riant', 'train']
        self.assertEqual(result, expected)

    def test_drive(self):
        result = anagrams("drive")
        expected = ['diver', 'drive', 'rived']
        self.assertEqual(result, expected)

    def test_python(self):
        result = anagrams("python")
        expected = ['phyton', 'python', 'typhon']
        self.assertEqual(result, expected)

    def test_empty_word(self):
        result = anagrams("")
        expected = []
        self.assertEqual(result, expected)

    def test_no_anagrams(self):
        result = anagrams("aaa")
        expected = []  # No anagrams expected for a word not in the list
        self.assertEqual(result, expected)

    def test_long_word(self):
        result = anagrams("pneumonoultramicroscopicsilicovolcanoconiosis")
        expected = []  # No anagrams expected

    def test_case_insensitivity(self):
        result_lower = anagrams("train")
        result_upper = anagrams("TRAIN")
        self.assertEqual(result_lower, result_upper)


if __name__ == "__main__":
    unittest.main()