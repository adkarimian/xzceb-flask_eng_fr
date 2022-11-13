import unittest
import translator

class Test(unittest.TestCase):
    def test_frenchToEnglish1(self):
        frenchText = None
        englishText = translator.french_to_english(frenchText)
        self.assertEqual(englishText, None)

    def test_frenchToEnglish2(self):
        frenchText = "Bonjour"
        englishText = translator.french_to_english(frenchText)
        self.assertEqual(englishText, 'Hello')

    def test_englishToFrench1(self):
        englishText = None
        frenchText = translator.english_to_french(englishText)
        self.assertEqual(frenchText, None)

    def test_englishToFrench2(self):
        englishText = "Hello"
        frenchText = translator.english_to_french(englishText)
        self.assertEqual(frenchText, 'Bonjour')

if __name__ == '__main__':
    unittest.main()