"""Test suite for config.py"""

# Importing necessary modules
import pytest
from TissueExp import config


def test_get_directory_for_unigene():
    """
    Testing whether it returns the correct directory for unigene data
    :return:
    """
    assert config.get_directory_for_unigene() == "./TissueExp_data", "Incorrect directory for unigene data"


def test_get_extension_for_unigene():
    """
    Testing whether it returns the correct file ending for unigene files
    :return:
    """
    assert config.get_extension_for_unigene() == "unigene", "Incorrect file ending for unigene files"


def test_get_keywords_for_hosts():
    """
    Testing whether it returns the correct dictionary mapping common names to scientific names for hosts
    :return:
    """
    expected_keywords = {
        "homo sapiens": "Homo_sapiens",
        "human": "Homo_sapiens",
        "humans": "Homo_sapiens",
        "bos taurus": "Bos_taurus",
        "cow": "Bos_taurus",
        "cows": "Bos_taurus",
        "equus caballus": "Equus_caballus",
        "horse": "Equus_caballus",
        "horses": "Equus_caballus",
        "mus musculus": "Mus_musculus",
        "mouse": "Mus_musculus",
        "mice": "Mus_musculus",
        "ovis aries": "Ovis_aries",
        "sheep": "Ovis_aries",
        "sheeps": "Ovis_aries",
        "rattus norvegicus": "Rattus_norvegicus",
        "rat": "Rattus_norvegicus",
        "rats": "Rattus_norvegicus",
    }
    assert config.get_keywords_for_hosts() == expected_keywords, "Incorrect dictionary for host keywords"


def test_get_error_string_4_ValueError(capsys):
    """
    Testing whether it prints the correct error message for ValueError
    :param capsys:
    :return:
    """
    config.get_error_string_4_ValueError()
    captured = capsys.readouterr()
    assert "Invalid argument Value for opening a file for reading/writing" in captured.out, "Incorrect error message"


def test_get_error_string_4_TypeError(capsys):
    """
    Testing whether it prints the correct error message for TypeError
    :param capsys:
    :return:
    """
    config.get_error_string_4_TypeError()
    captured = capsys.readouterr()
    assert "Invalid argument Type passed in:" in captured.out, "Incorrect error message"


def test_get_error_string_4_PermissionError(capsys):
    """
    Testing whether it prints the correct error message for PermissionError
    :param capsys:
    :return:
    """
    config.get_error_string_4_PermissionError(file="/test/file.txt")
    captured = capsys.readouterr()
    assert "Could not create the directory (permissions): /test/file.txt" in captured.out, "Incorrect error message"


def test_get_error_string_4_FileNotFoundError(capsys):
    """
    Testing whether it prints the correct error message for FileNotFoundError
    :param capsys:
    :return:
    """
    config.get_error_string_4_FileNotFoundError(file="/test/file.txt")
    captured = capsys.readouterr()
    assert ("Could not create the directory (invalid argument): /test/file.txt"
            in captured.out), "Incorrect error message"


def test_get_error_string_4_opening_file_OSError(capsys):
    """
    Testing whether it prints the correct error message for OSError when opening a file
    :param capsys:
    :return:
    """
    config.get_error_string_4_opening_file_OSError(file="/test/file.txt", mode="r")
    captured = capsys.readouterr()
    assert "Could not open the file (os error): /test/file.txt with mode r" in captured.out, "Incorrect error message"


def test_get_error_string_4_opening_directory_OSError(capsys):
    """
    Testing whether it prints the correct error message for OSError when opening/making a directory
    :param capsys:
    :return:
    """
    config.get_error_string_4_opening_directory_OSError(directory="/test/directory")
    captured = capsys.readouterr()
    assert "Could not open/make directory (os error): /test/directory" in captured.out, "Incorrect error message"


def test_add_numbers1():
    """
    Testing whether it correctly adds numbers with None as the optional value
    :return:
    """
    assert config.add_numbers1(3) == 3, "Incorrect addition with None as optional value"
    assert config.add_numbers1(3, 5) == 8, "Incorrect addition with specified optional value"


def test_add_numbers2():
    """
    Testing whether it correctly adds numbers with a default optional value
    :return:
    """
    assert config.add_numbers2(3) == 13, "Incorrect addition with default optional value"
    assert config.add_numbers2(3, 5) == 8, "Incorrect addition with specified optional value"


def test_add_numbers1_with_non_integer_value():
    """
    Testing whether add_numbers1 handles a non-integer value as the optional parameter
    :return:
    """
    with pytest.raises(TypeError, match="unsupported operand type"):
        config.add_numbers1(3, "abc")


def test_add_numbers2_with_non_integer_value():
    """
    Testing whether add_numbers2 handles a non-integer value as the optional parameter
    :return:
    """
    with pytest.raises(TypeError, match="unsupported operand type"):
        config.add_numbers2(3, "abc")


def test_get_filehandle_new_with_invalid_file():
    """
    Testing whether get_filehandle_new raises MyOSError for an invalid file
    :return:
    """
    with pytest.raises(config.MyOSError, match="Could not open the file"):
        config.get_filehandle_new(file='/nonexistent/file.txt', mode='r')


def test_get_filehandle_new_with_invalid_mode():
    """
    Testing whether get_filehandle_new raises MyOSError for an invalid mode
    :return:
    """
    with pytest.raises(config.MyOSError, match="Could not open the file"):
        config.get_filehandle_new(file='/valid/file.txt', mode='invalid_mode')


def test_get_filehandle_new_with_permission_denied():
    """
    Testing whether get_filehandle_new raises MyOSError for a permission denied scenario
    :return:
    """
    with pytest.raises(config.MyOSError, match="Permission denied"):
        config.get_filehandle_new(file='/protected/file.txt', mode='w')


def test_custom_exception_str_representation():
    """
    Testing the string representation of the custom exception
    :return:
    """
    my_error = config.MyOSError(file="/test/file.txt", mode="r", err="Custom error message")
    expected_str = "Error: Custom error message\nCould not open the file: /test/file.txt for type r"
    assert str(my_error) == expected_str, "Incorrect string representation of custom exception"


def test_custom_exception():
    """
    Testing whether the custom exception class works as expected
    :return:
    """
    my_error = config.MyOSError(file="/test/file.txt", mode="r", err="Permission denied")
    assert my_error.file == "/test/file.txt", "Incorrect file attribute in custom exception"
    assert my_error.mode == "r", "Incorrect mode attribute in custom exception"
    assert my_error.err == "Permission denied", "Incorrect err attribute in custom exception"
    assert str(my_error) == "Error: Permission denied\nCould not open the file: /test/file.txt in r mode"
