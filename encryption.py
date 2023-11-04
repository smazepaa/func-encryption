import ctypes

# Load the DLL
my_lib = ctypes.CDLL('C:/Users/sofma/source/func-encryption.git/encryption.dll')

# Declare the argument types and return type of your functions
my_lib.encrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_lib.encrypt.restype = ctypes.c_char_p
my_lib.decrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_lib.decrypt.restype = ctypes.c_char_p
my_lib.free_memory.argtypes = [ctypes.c_char_p]
my_lib.free_memory.restype = None

# Use the functions
text = b"your text"
number = 1
length = len(text)

encrypted_text = my_lib.encrypt(text, number, length)
print("Encrypted text:", encrypted_text.decode())

decrypted_text = my_lib.decrypt(encrypted_text, number, length)
print("Decrypted text:", decrypted_text.decode())

# Free the memory allocated by the DLL
my_lib.free_memory(encrypted_text)
my_lib.free_memory(decrypted_text)


def execute(command, get_text, key, output_text):
    encrypted_or_decrypted_text = command(get_text, key)
    output_text(encrypted_or_decrypted_text)
