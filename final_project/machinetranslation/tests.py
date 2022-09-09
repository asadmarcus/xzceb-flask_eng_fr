import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("Hello"), "non") # test not equal
        self.assertEqual(english_to_french("Laboratory"), "Laboratoire") # test equal
        self.assertEqual(english_to_french("hello"), "Bonjour" ) # test equal
        self.assertEqual(english_to_french(" "), " ") # test null

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Bonjour"), "one") # test not equal
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test equal
        self.assertEqual(french_to_english("Arbre"), "Tree") # test equal
        self.assertEqual(french_to_english(" "), " ") # test null

unittest.main()