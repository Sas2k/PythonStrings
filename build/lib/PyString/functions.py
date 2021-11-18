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