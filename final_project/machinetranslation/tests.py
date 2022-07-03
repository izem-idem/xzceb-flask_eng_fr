import unittest
from unittest import TestCase

import translator  as tran

class TestTranslator(TestCase):

    def test_translation(self):
        self.assertEqual(tran.english_to_french('Hello'), 'Bonjour') # test when 'hello' is given as input
    def test_translation_2(self):
        self.assertEqual(tran.french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input
    def test_null_input(self):
        self.assertRaises(ValueError,tran.english_to_french,None) # Test for null input for englishToFrench
    def test_null_input_2(self):
        self.assertRaises(ValueError,tran.french_to_english,None) # Test for null input for french_to_english


if __name__=='__main__':
    unittest.main()
