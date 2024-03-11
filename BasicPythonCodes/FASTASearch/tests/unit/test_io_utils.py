"""Test suite for io_utils.py"""
import os
import pytest

from FASTASeach.io_utils import (get_filehandle)

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_filehandle_for_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

FILE_TO_TEST = "test.txt"
FILE_TO_TEST_INPUT = ""
FILE_TO_TEST_PARSING = "test.fasta"
FASTA_STRING = """\
>TEST1:A:sequence
GVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLKTEAEMKASEDLKKHGVTVLTALGA
MLKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKEL
TYQG
>TEST1:A:secstr
    THHHHHHHHHHHHHGGGHHHHHHHHHHHHHHH GGGGGG TTTTT  SHHHHHH HHHHHHHHHHHHHHHH
HHTTHT  HHHHHHHHHHHHHTS   HHHHHHHHHHHHHHHHHH GGG SHHHHHHHHHHHHHHHHHHHHHHHHT
T
>TEST2:A:sequence
GNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAA
MRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRV
TTTFRTGTWDAYKNL
>TEST2:A:secstr
  THHHHHHHH  EEEEEE TTS EEEETTEEEESSS TTTHHHHHHHHHHTS  TTB  HHHHHHHHHHHHHHH
THHHHH TTHHHHHHHS HHHHHHHHHHHHHHHHHHHHT HHHHHHHHTT HHHHHHHHHSSHHHHHSHHHHHHH
THHHHHSSSGGG
"""


def test_existing_get_filehandle_for_reading():
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    # does it open a file for writing
    # test
    test = get_filehandle(file=FILE_TO_TEST, mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_ValueError():
    # does it raise ValueError
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def _create_file_for_testing(file):
    # not actually run, the are just helper funnctions for the test script
    # create a test file
    open(file, "w").close()


def _create_fasta_file_for_testing():
    fh = open(FILE_TO_TEST_PARSING, "w")
    fh.write(FASTA_STRING)
    fh.close()
