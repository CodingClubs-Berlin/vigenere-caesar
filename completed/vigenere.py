import sys
import math
from vigenere_help_functions import *


def getText():
    print("Please insert the text you want to en-/decode")
    text = getInput()
    return text
    

def getKey():
    print("Please insert the key you want to use for en-/decryption")
    letter = getInput()
    return letter


def getCodeing():
    print("If you want to encode type 'en'.")
    print("If you want to decode type 'de'.")
    coding = getInput()
    if (sameString(coding, "en") == False and sameString(coding, "de") == False):
        print("Type one of both!")
        coding = getCodeing()
    return coding


def encrypt(text, key):
    for i in range (0, len(text)):
        text[i] = add_characters(text[i], key[i % len(key)])
    return text


def decrypt(text, key):
    for i in range (0, len(text)):
        text[i] = sub_characters(text[i], key[i % len(key)])
    return text


def vigenere():
    text = getText()
    key = getKey()
    coding = getCodeing()
    if (sameString(coding, "en") == True):
        new_text = encrypt(text, key)
    else:
        new_text = decrypt(text, key)
    print("The en-/decrypted text is:")
    printText(new_text)

vigenere()