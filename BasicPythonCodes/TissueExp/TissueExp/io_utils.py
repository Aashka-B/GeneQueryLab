"""
File:  io_utils.py

This module processes command line user input files.
"""

# Importing necessary modules
import os
from typing import IO

# Absolute Module Import
from TissueExp import config


# Defining functions
def get_filehandle(file: str, mode: str) -> IO:
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments fh_in name and mode i.e. what is needed to be done with
    this fh_in. This function opens the fh_in based on the mode passed in
    the argument and returns filehandle.
    @param file: The fh_in to open for the mode
    @param mode: They way to open the fh_in, e.g. reading, writing, etc
    @return: filehandle
    """
    try:
        fobj = open(file=file, mode=mode)
        return fobj
    except OSError:
        config.get_error_string_4_opening_file_OSError(file=file, mode=mode)
        # raising like this allows the overall application to choose whether
        # to stop running gracefully or handle the exception.
        # you could have a function you implement like log_the_error(err), and then raise
        raise
    except ValueError:  # test something like io_utils.get_filehandle("does_not_exist.txt", "rrr")
        config.get_error_string_4_ValueError()
        raise
    except TypeError:  # test something like io_utils.get_filehandle([], "r")
        config.get_error_string_4_TypeError()
        raise


def mkdir_from_infile(file: str) -> None:
    """
    void : mkdir_from_infile("/home/cleslin/test.txt")
    Takes : 1 argument, tries to create a directory from an infile string passed in
    @param file: The fh_in it will then try and make a directory from it's root
    @return: None
    """
    try:
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
    except PermissionError:
        config.get_error_string_4_PermissionError(file=file)
        raise
    except FileNotFoundError:
        # if the fh_in is only a string with no /, you'll get : No such fh_in or directory: ''
        config.get_error_string_4_FileNotFoundError(file=file)
        raise
    except OSError:
        config.get_error_string_4_opening_directory_OSError(directory=file)
        raise


def is_gene_file_valid(file_name: str) -> bool:
    """
    Checks if the given file exists.
    """
    return os.path.exists(file_name)
