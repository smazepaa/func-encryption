from encryption import execute, encrypt, decrypt
from filestream import read_file, write_file, read_console, write_console


def process_command(source, command, where_to, key, file_i=None, file_o=None):
    if source == "file":
        get_text = read_file(file_i)
    elif source == "console":
        get_text = read_console
    else:
        print("Invalid source")
        return

    if command == "encrypt":
        cmd = encrypt
    elif command == "decrypt":
        cmd = decrypt
    else:
        print("Invalid command")
        return

    if where_to == "console":
        output_text = write_console
    elif where_to == "file":
        output_text = lambda text: write_file(file_o, text)
    else:
        print("Invalid output")
        return

    execute(cmd, get_text, key, output_text)
