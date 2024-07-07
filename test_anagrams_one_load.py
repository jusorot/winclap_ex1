import unittest
from anagrams_one_load import anagrams

class TestAnagrams(unittest.TestCase):
    def setUp(self):
        # Load list
        with open('WORD.lst') as file:
            self.words = [w.rstrip().lower() for w in file]

    def test_train(self):
        result = anagrams("train", self.words)
        expected = ['riant', 'train']
        self.assertEqual(result, expected)

    def test_drive(self):
        result = anagrams("drive", self.words)
        expected = ['diver', 'drive', 'rived']
        self.assertEqual(result, expected)

    def test_python(self):
        result = anagrams("python", self.words)
        expected = ['phyton', 'python', 'typhon']
        self.assertEqual(result, expected)

    def test_empty_word(self):
        result = anagrams("", self.words)
        expected = []
        self.assertEqual(result, expected)

    def test_no_anagrams(self):
        result = anagrams("aaa", self.words)
        expected = []
        self.assertEqual(result, expected)

    def test_long_word(self):
        result = anagrams("pneumonoultramicroscopicsilicovolcanoconiosis", self.words)
        expected = []
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        result_lower = anagrams("train", self.words)
        result_upper = anagrams("TRAIN", self.words)
        self.assertEqual(result_lower, result_upper)

if __name__ == "__main__":
    unittest.main()

