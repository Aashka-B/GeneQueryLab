"""Test suite for module py"""

# Importing necessary modules
import os
import pytest

from TissueExp.io_utils import get_filehandle, mkdir_from_infile, is_gene_file_valid

# Defining a dummy test file
FILE_2_TEST = "test.txt"


# Defining function
def test_existing_get_filehandle_for_reading():
    """
    Testing whether it opens a file for reading
    :return:
    """
    # create a test file
    _create_test_file(FILE_2_TEST)
    # test
    test = get_filehandle(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_filehandle_for_writing():
    """
    Testing whether it opens a file for writing
    :return:
    """
    # test
    test = get_filehandle(FILE_2_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_filehandle_for_OSError():
    """
    Testing whether it raises an OSError
    :return:
    """
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_ValueError():
    """
    Testing whether it raises a ValueError
    :return:
    """
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_2_TEST)


def test_get_filehandle_for_TypeError():
    """
    Testing whether it raises a TypeError
    :return:
    """
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        get_filehandle([], "r")
    os.remove(FILE_2_TEST)


def test_mkdir_from_infile():
    """
    Testing whether you create a directory from a string like 'test/test.txt'
    :return:
    """
    # create a test file
    file = 'test/test.txt'
    dir_ = os.path.dirname(file)
    mkdir_from_infile(file)
    assert os.path.exists(dir_) is True, "Not able to create a directory from 'test/test.txt'"

    os.rmdir(dir_)  # removes an empty directory.


def test_mkdir_from_directory_only():
    """
    Testing whether you create a directory from a string like 'test/'
    :return:
    """
    # create a test file
    file = 'test/'
    dir_ = os.path.dirname(file)
    mkdir_from_infile(file)
    assert os.path.exists(dir_) is True, "Not able to create a directory from 'test/'"

    os.rmdir(dir_)  # removes an empty directory.


def test_mkdir_from_infile_with_existing_directory(tmp_path):
    """

    :param tmp_path:
    :return:
    """
    # Use tmp_path to create a temporary directory
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()

    # Test
    mkdir_from_infile(dir_path)
    assert os.path.exists(dir_path), "Failed to create a directory from an existing directory"


def test_mkdir_from_infile_with_invalid_path():
    """
    Testing whether it creates a directory from an invalid path
    :return:
    """
    # Test
    with pytest.raises(FileNotFoundError):
        mkdir_from_infile("/invalid/path/that/does/not/exist")


def test_mkdir_from_with_file_OSError():
    """
    Testing whether it raises an OSError
    :return:
    """
    # create a test file
    file = '/OUTPUT_CANT_BE_MADE_IN_ROOT/test.txt'
    with pytest.raises(OSError):
        mkdir_from_infile(file)


def test_mkdir_from_with_file_PermissionError():
    """
    Testing whether it raises a PermissionError
    :return:
    """
    # will not be able to make directory here
    file = '/Users/will_not_be_able_to_make/test.txt'
    with pytest.raises(PermissionError):
        mkdir_from_infile(file)


def test_mkdir_from_with_file_FileNotFoundError():
    """
    Testing whether it raises a FileNotFoundError
    :return:
    """
    # create a test file
    file = 'test.txt'
    with pytest.raises(FileNotFoundError):
        mkdir_from_infile(file)


def test_is_gene_file_valid():
    """
    Testing whether it correctly identifies an existing file
    :return:
    """
    # create a test file
    _create_test_file(FILE_2_TEST)
    # test
    assert is_gene_file_valid(FILE_2_TEST) is True, "Not able to identify an existing file"
    os.remove(FILE_2_TEST)


def test_is_gene_file_valid_nonexistent():
    """
    Testing whether it correctly identifies a non-existing file
    :return:
    """
    # test
    assert is_gene_file_valid("nonexistent_file.txt") is False, "Incorrectly identified a non-existing file"


def test_is_gene_file_valid_directory():
    """
    Testing whether it correctly identifies a directory as invalid
    :return:
    """
    # create a test directory
    os.makedirs("test_directory")
    # test
    assert is_gene_file_valid("test_directory") is False, "Incorrectly identified a directory as a valid file"
    os.rmdir("test_directory")


def test_is_gene_file_valid_with_invalid_path():
    """
    Testing whether it correctly identifies an invalid path
    :return:
    """
    # Test
    assert is_gene_file_valid("/invalid/path/that/does/not/exist") is False, \
        "Incorrectly identified an invalid path as a valid file"


def test_create_test_file():
    """
    Test whether _create_test_file creates a file successfully.
    """
    _create_test_file("test_create_test_file.txt")
    assert os.path.exists("test_create_test_file.txt"), "Failed to create the test file"
    os.remove("test_create_test_file.txt")


def _create_test_file(file):
    """
    A helper function for the test script
    :param file:
    :return:
    """
    # create a test file
    open(file, "w").close()


if __name__ == '__main__':
    file_2_test = '/Users/will_not_be_able_to_make/test.txt'
    mkdir_from_infile(file_2_test)
