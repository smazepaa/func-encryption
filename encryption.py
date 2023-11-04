# def encrypt(text, key):
#     return ''.join(chr(ord(c) + key) for c in text)

# def encrypt_full(text, number):
#     result = ""
#     for i in text:
#         ascii_value = ord(i)
#         new_ascii_value = ascii_value + number
#         new_character = chr(new_ascii_value)
#         result += new_character
#     return result

# def decrypt(text, key):
#     return ''.join(chr(ord(c) - key) for c in text)


encrypt = lambda text, key: ''.join(chr((ord(c) + key) % 128) for c in text)
decrypt = lambda text, key: ''.join(chr((ord(c) - key) % 128) for c in text)


# command - function to encrypt/decrypt
# get_text - function to get from console/file
# output_text - function to get from console/file

def execute(command, get_text, key, output_text):
    encrypted_or_decrypted_text = command(get_text, key)
    output_text(encrypted_or_decrypted_text)
