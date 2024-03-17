import pandas as pd


def read_from_console():
    """
    Reads data from console

    Returns:
        str: data from console
    """
    console_text = input("Enter text: ")
    return console_text


def read_from_file(file_name):
    """
    Reads data from file using python build-in python methods

    Args:
        file_name (str): file to read data from

    Returns:
        str: data from file
    """
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{file_name}' not found"


def read_from_csv_file_with_pandas(file_name):
    """
    Reads data from csv file using pandas

    Args:
        file_name (str): csv file to read data from

    Returns:
        str: data from file
    """
    try:
        file_data = pd.read_csv(file_name)
        return file_data.to_string()
    except FileNotFoundError:
        return f"File '{file_name}' not found"
