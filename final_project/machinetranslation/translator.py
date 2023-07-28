"""This module has the functions n charge of translating between english and french"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """This function translates english text `english_text` to french"""
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """This function translates french text `french_text` to english"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
