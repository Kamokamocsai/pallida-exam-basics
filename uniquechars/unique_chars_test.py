import unittest
from unique_chars import unique_characters

class LetterCounterTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(unique_characters('aa'), [''])
    
    # def test_one_letter(self):
    #     self.assertEqual(unique_characters("aaa"), [])
    #     self.assertEqual(unique_characters("aab"), [])

    # def test_two_different_letters(self):
    #     self.assertEqual(unique_characters("aaab"), [])

    # def test_two_same_letters(self):
    #     self.assertEqual(unique_characters("aaaa"), [])
        

if __name__ == '__main__':
    unittest.main()