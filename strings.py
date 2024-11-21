import string

def uppercase(words):
    return string.ascii_uppercase(words)

def lowercase(words):
    return string.ascii_lowercase(words)

def utf8(words):
    return str(words).encode(str = "utf-8")