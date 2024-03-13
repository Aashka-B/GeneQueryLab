"""
File:  config.py

This module is used for configuration.
It is used to process Unigene data files,
to get host keywords from the user,
and for error printing.
"""
# Importing necessary modules
from typing import IO, Optional

# Creating variables
_DIRECTORY_FOR_UNIGENE = "./TissueExp_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


# Defining functions
def get_directory_for_unigene() -> str:
    """
    Returns the directory for unigene data.
    :return:
    """
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene() -> str:
    """
    Returns the file ending for unigene files.
    :return:
    """
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts() -> dict:
    """
    Returns a dictionary mapping common names to scientific names for hosts.
    :return:
    """
    host_keywords = {
        "Homo sapiens": "Homo_sapiens",
        "Human": "Homo_sapiens",
        "Humans": "Homo_sapiens",
        "Bos taurus": "Bos_taurus",
        "Cow": "Bos_taurus",
        "Cows": "Bos_taurus",
        "Equus caballus": "Equus_caballus",
        "Horse": "Equus_caballus",
        "Horses": "Equus_caballus",
        "Mus musculus": "Mus_musculus",
        "Mouse": "Mus_musculus",
        "Mice": "Mus_musculus",
        "Ovis aries": "Ovis_aries",
        "Sheep": "Ovis_aries",
        "Sheeps": "Ovis_aries",
        "Rattus norvegicus": "Rattus_norvegicus",
        "Rat": "Rattus_norvegicus",
        "Rats": "Rattus_norvegicus",
    }
    return host_keywords


def get_error_string_4_ValueError() -> None:  # error when used get_filehandle(fh_in, "1234")
    """
    Print the invalid argument message for ValueError
    :return:
    """
    print("Invalid argument Value for opening a fh_in for reading/writing")


def get_error_string_4_TypeError() -> None:  # error when used get_filehandle(fh_in, "r", "w")
    """
    Print the invalid argument message for TypeError
    :return:
    """
    print("Invalid argument Type passed in:")


def get_error_string_4_PermissionError(file: str) -> None:
    """
    Print the invalid argument message for PermissionError
    @param file: The fh_in name
    """
    print(f"Could not create the directory (permissions): {file}")


def get_error_string_4_FileNotFoundError(file: str) -> None:
    """
    Print the invalid argument message for FileNotFoundError
    @param file: The fh_in name
    """
    print(f"Could not create the directory (invalid argument): {file}")


def get_error_string_4_opening_file_OSError(file: str, mode: str) -> None:
    """
    Print the invalid argument message for OSError
    @param file: The fh_in name
    @param mode: The mode to open the fh_in
    """
    print(f"Could not open the fh_in (os error): {file} with mode {mode}")


def get_error_string_4_opening_directory_OSError(directory: str) -> None:
    """
    Print the invalid argument message for OSError when open/making a directory
    @param directory: The directory opened
    """
    print(f"Could not open/make directory (os error): {directory}")


def add_numbers1(num1: int, num2: Optional[int] = None) -> int:
    """
    Was not required to be implemented for this assignment, but wanted show how to have a None optional value
    @param num1: int
    @param num2: int
    @return: int
    """
    if num2 is None:
        num2 = 0
    return num1 + num2


def add_numbers2(num1: int, num2: int = 10) -> int:
    """
    Was not required to be implemented for this assignment, but wanted show how to have an  optional value with a
    default
    @param num1: int
    @param num2: int
    @return: int
    """
    return num1 + num2


class MyOSError(Exception):
    """Custom Exception raised for errors with OSError

    Takes : 2 arguments
    The fh_in name
    The mode that was passed in
    """
    def __init__(self, file=None, mode=None, err=None):
        self.file = file
        self.mode = mode
        self.err = err
        self.message = f"Error: {err}\nCould not open the fh_in': {self.file} for type {self.mode}"
        super().__init__(self.message)


def get_filehandle_new(file: str, mode: str) -> IO:
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments fh_in name and mode i.e. what is needed to be done with
    this fh_in. This function opens the fh_in based on the mode passed in
    the argument and returns filehandle.
    @param file: File to open
    @param mode: What mode to open the fh_in
    @return: filehandle
    """
    try:
        fobj = open(file, mode)
        return fobj
    except OSError as err:
        raise MyOSError(file=file, mode=mode, err=err) from None


def _test_custom_exception() -> None:
    """
    Testing custom MyOSError exception
    :return:
    """
    print("testing get_filehandle_new\n")
    try:
        get_filehandle_new(file='junk.txt', mode='r')
    except MyOSError as err:
        print("Error message (code will continue:")
        print(err)

    print("\n\ntesting get_filehandle_new with no try except\n")

    get_filehandle_new(file='junk.txt', mode='r')


if __name__ == '__main__':
    print("Showing an example of Typing with Optional values")
    print(add_numbers1(3))
    print(add_numbers2(3))
    print("\n\n")
    _test_custom_exception()
