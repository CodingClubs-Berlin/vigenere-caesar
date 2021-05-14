import sys
import math
from caesar_help_functions import *


def getText():
    print("Please insert the text you want to en-/decode")
    text = getInput()
    return text
    

def getLetter():
    print("Please insert the letter you want to use for en-/decryption")
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


def encrypt(text, letter):
    for i in range (0, len(text)):
        text[i] = add_characters(text[i], letter)
    return text


def decrypt(text, letter):
    for i in range (0, len(text)):
        text[i] = sub_characters(text[i], letter)
    return text


def caesar():
    text = getText()
    letter = getLetter()
    while (len(letter) != 1):
        print("That was not only a single letter...")
        letter = getLetter()
    coding = getCodeing()
    if (sameString(coding, "en") == True):
        new_text = encrypt(text, letter)
    else:
        new_text = decrypt(text, letter)
    print("The en-/decrypted text is:")
    printText(new_text)

caesar()