def revstring(string):
    string = str(string)
    return string[::-1]

def encodestr(string):
    string = str(string)
    string_utf = string.encode("utf_16")
    return string_utf

def decodestr(string):
    orstring = string.decode("utf-16")
    return orstring

def Capatilize(string):
    string = string.capitalize()
    return string

def Cap(string):
    string = len(string)
    return len(string)