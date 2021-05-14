

possible = [c for c in (chr(i) for i in range(32,127))]
def add_characters(charOne, charTwo):
    txt_idx = possible.index(charOne)
    key_idx = possible.index(charTwo)
    ret = possible[(txt_idx + key_idx) % len(possible)]
    return (ret)


def sub_characters(charOne, charTwo):
    txt_idx = possible.index(charOne)
    key_idx = possible.index(charTwo)
    ret = possible[(txt_idx - key_idx) % len(possible)]
    return (ret)


def printText(new_text):
    print("".join(new_text))


def getInput():
    return list(input())



def sameString(str1, str2):
    return str2 == "".join(str1)