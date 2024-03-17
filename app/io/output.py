def write_to_console(text):
    """
    Write text to console

    Args:
        text (str): text to print to console
    """
    print(text)


def write_to_file(text, file_name):
    """
    Write text to file using build-in python methods

    Args:
        text (str): text to write to a file
    """
    with open(file_name, "w") as file:
        file.write(text)
