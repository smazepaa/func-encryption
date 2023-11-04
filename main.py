from encryption import encrypt, decrypt

text = "abc"
encrypted = encrypt(text, 2)
print(encrypted)

decrypted = decrypt(encrypted, 2)
print(decrypted)
