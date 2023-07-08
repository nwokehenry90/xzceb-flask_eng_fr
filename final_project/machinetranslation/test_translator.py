import unittest

from .translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hi')


    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hi')
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')


if __name__ == "__main__":
    unittest.main()
