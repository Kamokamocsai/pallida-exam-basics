import unittest
from unique_chars import unique_characters

class LetterCounterTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(unique_characters(''), [])
    
    def test_one_letter(self):
        self.assertEqual(unique_characters("a"), ['a'])
        self.assertEqual(unique_characters("b"), ['b'])

    def test_two_different_letters(self):
        self.assertEqual(unique_characters("ab"), ['a', 'b'])

    def test_two_same_letters(self):
        self.assertEqual(unique_characters("aa"), [])
        
    def test_two_same_letters_with_more(self):
        self.assertEqual(unique_characters("abrakadabra"), ['k', 'd'])


if __name__ == '__main__':
    unittest.main()