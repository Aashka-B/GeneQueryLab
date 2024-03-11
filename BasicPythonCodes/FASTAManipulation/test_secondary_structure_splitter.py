"""
A test script for the secondary_structure_splitter.py program.
"""
import pytest
from secondary_structure_splitter import (get_fasta_lists, get_filehandle,
                                          output_results_to_files, _verify_lists)


# Define test cases for each function
def test_get_filehandle(tmp_path):
    """
    testing the get_filehandle() function
    """
    # Test case 1: Basic test with a valid file
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as file:
        file.write("Test content")

    fh_in = get_filehandle(file_path, "r")
    assert fh_in is not None
    fh_in.close()

    # Test case 2: Non-existent file, should raise an exception
    non_existent_file = tmp_path / "non_existent.txt"
    with pytest.raises(SystemExit):
        get_filehandle(non_existent_file, "r")

    # Test case 3: Read and write mode
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as file:
        file.write("Test content")

    fh_out = get_filehandle(file_path, "w")
    assert fh_out is not None
    fh_out.write("Additional content")
    fh_out.close()

    with open(file_path, "r") as file:
        content = file.read()
    assert content == "Additional content"

    # Test case 4: Invalid file mode, should raise an exception
    invalid_mode = tmp_path / "test_file.txt"
    with pytest.raises(SystemExit):
        get_filehandle(invalid_mode, "invalid_mode")


def test_get_filehandle_4_os_error():
    """
    testing the get_filehandle() function for an OS Error
    """

    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")

    file_name = "test_file.txt"
    mode = "w"
    with get_filehandle(file_name, mode) as fh:
        assert fh.mode == "w"


def test_get_fasta_lists():
    """
    testing the get_fasta_lists() function
    """

    # Test case 1: Basic test with one protein sequence and one secondary structure
    input_data = [
        ">Header1",
        "ProteinSequence1",
        ">Header2",
        "SecondaryStructure1",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["ProteinSequence1", "SecondaryStructure1"]

    # Test case 2: Multiple protein sequences and secondary structures
    input_data = [
        ">Header1",
        "ProteinSequence1",
        ">Header2",
        "SecondaryStructure1",
        ">Header3",
        "ProteinSequence2",
        ">Header4",
        "SecondaryStructure2",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1", "Header2", "Header3", "Header4"]
    assert sequence_list == ["ProteinSequence1", "SecondaryStructure1", "ProteinSequence2", "SecondaryStructure2"]

    # Test case 3: Empty lines and extra whitespaces
    input_data = [
        ">Header1",
        "",
        "ProteinSequence1",
        "    ",
        ">Header2",
        "  SecondaryStructure1  ",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["ProteinSequence1", "SecondaryStructure1"]

    # Test case 4: Missing header for the last sequence
    input_data = [
        ">Header1",
        "ProteinSequence1",
        "SecondaryStructure1",
    ]
    with pytest.raises(SystemExit):
        get_fasta_lists(input_data)  # Should exit with an error

    # Test case 5: No data in the input
    input_data = []
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == []
    assert sequence_list == []

    # Test case 6: Only secondary structure data
    input_data = [
        ">Header1",
        "SecondaryStructure1",
        ">Header2",
        "SecondaryStructure2",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["SecondaryStructure1", "SecondaryStructure2"]

    # Test case 7: Complex input with mixed headers and sequences
    input_data = [
        ">Header1",
        "ProteinSequence1",
        "SecondaryStructure1",
        ">Header2",
        "",
        "ProteinSequence2",
        ">Header3",
        "SecondaryStructure2",
        "    ",
        ">Header4",
        "SecondaryStructure3",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1", "Header2", "Header3", "Header4"]
    assert sequence_list == ["ProteinSequence1", "SecondaryStructure1", "ProteinSequence2", "SecondaryStructure2"]

    # Test case 8: Complex input with line breaks within sequences
    input_data = [
        ">Header1",
        "ProteinSequence1",
        "Line1",
        "Line2",
        "SecondaryStructure1",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1"]
    assert sequence_list == ["ProteinSequence1Line1Line2SecondaryStructure1"]

    # Test case 9: Complex input with line breaks within sequences and empty lines
    input_data = [
        ">Header1",
        "",
        "ProteinSequence1",
        "Line1",
        "  ",
        "Line2",
        "",
        "SecondaryStructure1",
    ]
    header_list, sequence_list = get_fasta_lists(input_data)
    assert header_list == ["Header1"]
    assert sequence_list == ["ProteinSequence1Line1Line2SecondaryStructure1"]


def test_verify_lists():
    """
    testing the _verify_lists() function
    """

    # Test case 1: Lists have the same length
    header_list = ["Header1", "Header2"]
    sequence_list = ["Sequence1", "Sequence2"]
    _verify_lists(header_list, sequence_list)  # Should not raise an error

    # Test case 2: Lists have different lengths
    header_list = ["Header1", "Header2"]
    sequence_list = ["Sequence1"]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should exit with an error

    # Test case 3: Empty lists
    header_list = []
    sequence_list = []
    _verify_lists(header_list, sequence_list)  # Should not raise an error

    # Test case 4: Lists with one empty element
    header_list = ["Header1"]
    sequence_list = [""]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should exit with an error

    # Test case 5: Lists with multiple empty elements
    header_list = ["Header1", "Header2"]
    sequence_list = ["", ""]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should exit with an error

    # Test case 6: Lists with whitespace-only elements
    header_list = ["Header1", "Header2"]
    sequence_list = ["   ", "  "]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should exit with an error

    # Test case 7: Lists with mixed valid and empty elements
    header_list = ["Header1", "Header2"]
    sequence_list = ["Sequence1", "", "Sequence3"]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should exit with an error


def test_output_results_to_files():
    """
    testing the output_results_to_files() function
    """

    # Test case 1: Basic test with two protein sequences and secondary structures
    header_list = ["Header1", "Header2"]
    sequence_list = ["ACGT", "GTCAGT"]

    output_file1 = "test_output1.txt"
    output_file2 = "test_output2.txt"

    with open(output_file1, "w", encoding="utf-8") as fh_out1, open(output_file2, "w", encoding="utf-8") as fh_out2:
        num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

        assert num_proteins == 2
        assert num_ss == 2

    with open(output_file1, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Header1\nACGT\n"

    with open(output_file2, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Header2\nGTCAGT\n"

    # Test case 2: Test with no data
    header_list = []
    sequence_list = []

    output_file1 = "test_output1.txt"
    output_file2 = "test_output2.txt"

    with open(output_file1, "w", encoding="utf-8") as fh_out1, open(output_file2, "w", encoding="utf-8") as fh_out2:
        num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

        assert num_proteins == 0
        assert num_ss == 0

    with open(output_file1, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == ""

    with open(output_file2, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == ""

    # Test case 3: Test with no secondary structure data
    header_list = ["Header1", "Header2"]
    sequence_list = ["ACGT", "GTCAGT"]

    output_file1 = "test_output1.txt"
    output_file2 = "test_output2.txt"

    with open(output_file1, "w", encoding="utf-8") as fh_out1, open(output_file2, "w", encoding="utf-8") as fh_out2:
        num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

        assert num_proteins == 2
        assert num_ss == 0

    with open(output_file1, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Header1\nACGT\nHeader2\nGTCAGT\n"

    with open(output_file2, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == ""

    # Test case 4: Test with empty protein sequences
    header_list = ["Header1", "Header2"]
    sequence_list = ["", "GTCAGT", "", "AAT"]

    output_file1 = "test_output1.txt"
    output_file2 = "test_output2.txt"

    with open(output_file1, "w", encoding="utf-8") as fh_out1, open(output_file2, "w", encoding="utf-8") as fh_out2:
        num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

        assert num_proteins == 2
        assert num_ss == 1

    with open(output_file1, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Header2\nGTCAGT\nHeader4\nAAT\n"

    with open(output_file2, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == ""

    # Test case 5: Test with empty secondary structure data
    header_list = ["Header1", "Header2"]
    sequence_list = ["ACGT", "", "GTCAGT", "", "AAT"]

    output_file1 = "test_output1.txt"
    output_file2 = "test_output2.txt"

    with open(output_file1, "w", encoding="utf-8") as fh_out1, open(output_file2, "w", encoding="utf-8") as fh_out2:
        num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

        assert num_proteins == 2
        assert num_ss == 1

    with open(output_file1, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Header1\nACGT\nHeader3\nGTCAGT\nHeader5\nAAT\n"

    with open(output_file2, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == ""


# Run the tests
if __name__ == "__main__":
    pytest.main()
