def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text


def write_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)


def read_console():
    text = input("Enter text: ")
    return text


def write_console(text):
    print("Output text:", text)
