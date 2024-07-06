from anagrams_scalable import preprocess_words, anagrams
import unittest

class TestAnagrams(unittest.TestCase):
    def setUp(self):
        # Preprocessing
        self.anagrams_dict = preprocess_words('WORD.lst')

    def test_train(self):
        result = anagrams("train", self.anagrams_dict)
        expected = ['riant', 'train']
        self.assertEqual(result, expected)

    def test_drive(self):
        result = anagrams("drive", self.anagrams_dict)
        expected = ['diver', 'drive', 'rived']
        self.assertEqual(result, expected)

    def test_python(self):
        result = anagrams("python", self.anagrams_dict)
        expected = ['phyton', 'python', 'typhon']
        self.assertEqual(result, expected)

    def test_empty_word(self):
        result = anagrams("", self.anagrams_dict)
        expected = []
        self.assertEqual(result, expected)

    def test_no_anagrams(self):
        result = anagrams("aaa", self.anagrams_dict)
        expected = [] 
        self.assertEqual(result, expected)

    def test_long_word(self):
        result = anagrams("pneumonoultramicroscopicsilicovolcanoconiosis", self.anagrams_dict)
        expected = [] 
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        result_lower = anagrams("train", self.anagrams_dict)
        result_upper = anagrams("TRAIN", self.anagrams_dict)
        self.assertEqual(result_lower, result_upper)

if __name__ == "__main__":
    unittest.main()
