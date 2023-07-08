"""This Module translates from french to english and vice versa"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Function english to french"""
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def frenchToEnglish(french_text):
    """Function french to english"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    print(english_text)
    return english_text
