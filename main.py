from processing import process_command
from filestream import read_console

source = input("How do you want to input text? ")
console_i = read_console() if source == "console" else None
file_i = input("Enter path to the input file: ") if source == "file" else None

where_to = input("How do you want to output text? ")
file_o = input("Enter path to the output file: ") if where_to == "file" else None

command = input("Do you want to encrypt or decrypt? ")
key = int(input("Enter a key: "))

process_command(source, command, where_to, key, file_i, file_o, console_i)
