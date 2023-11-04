import ctypes

# Load the DLL
my_lib = ctypes.CDLL('C:/Users/sofma/source/func-encryption.git/encryption.dll')

# Declare the argument types and return type of your functions
my_lib.encrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_lib.encrypt.restype = ctypes.c_char_p
my_lib.decrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_lib.decrypt.restype = ctypes.c_char_p


encrypt = lambda text, key: my_lib.encrypt(text.encode(), key, len(text)).decode()
decrypt = lambda text, key: my_lib.decrypt(text.encode(), key, len(text)).decode()


def execute(command, get_text, key, output_text):
    result = command(get_text, key)
    output_text(result)
