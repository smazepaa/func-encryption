def encrypt(text, number):
    return ''.join(chr(ord(c) + number) for c in text)


def decrypt(text, number):
    return ''.join(chr(ord(c) - number) for c in text)
