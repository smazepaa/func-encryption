from encryption import execute, encrypt, decrypt
from filestream import read_file, write_file, read_console, write_console

text = "abc"

source = input("how you want to input text? ")
where_to = input("how you want to output text? ")
command = input("do you want to encrypt or decrypt? ")
key = int(input("enter a key: "))

if source == "file":
    file_i = input("enter path to the input file: ")
    if command == "encrypt":
        if where_to == "console":
            # file_o = input("enter path to the output file: ")
            execute(encrypt, read_file(file_i), key, write_console)
