"""
A test script for the nt_fasta_stats.py program.
"""
import pytest
from nt_fasta_stats import (get_filehandle, get_fasta_lists, _verify_lists,
                            _get_num_nucleotides, _get_ncbi_accession,
                            calculate_gc_content, output_results_to_files)


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


def test_get_fasta_lists():
    """
    testing the get_fasta_lists() function
    """

    # Test case 1: Basic test with two sequences
    fh_in = ">Header1\nACGT\n>Header2\nGTCAGT"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["ACGT", "GTCAGT"]

    # Test case 2: Empty sequence
    fh_in = ">Header1\n\n>Header2\nGTCAGT"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["", "GTCAGT"]

    # Test case 3: Sequence with line breaks
    fh_in = ">Header1\nACGT\nAGCT\n>Header2\nGTCAGT\nCAGTC"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["ACGTAGCT", "GTCAGTCAGTC"]

    # Test case 4: No header, should ignore
    fh_in = "ACGT\n>Header2\nGTCAGT"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header2"]
    assert sequence_list == ["GTCAGT"]

    # Test case 5: Empty input, should return empty lists
    fh_in = ""
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == []
    assert sequence_list == []

    # Test case 6: Multiple empty lines and spaces
    fh_in = ">Header1\n\n   \n\n>Header2\n  \nGTCAGT"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["", "GTCAGT"]

    # Test case 7: Special characters in sequence
    fh_in = ">Header1\nACGT!@#\n>Header2\nGTCAGT$%^&"
    header_list, sequence_list = get_fasta_lists(fh_in)
    assert header_list == ["Header1", "Header2"]
    assert sequence_list == ["ACGT!@#", "GTCAGT$%^&"]


def test_verify_lists():
    """
    testing the _verify_lists() function
    """

    # Test case 1: Header and sequence lists of the same size
    header_list = ["Header1", "Header2"]
    sequence_list = ["ACGT", "GTCAGT"]
    _verify_lists(header_list, sequence_list)  # Should not raise an exception

    # Test case 2: Header list is longer
    header_list = ["Header1", "Header2", "Header3"]
    sequence_list = ["ACGT", "GTCAGT"]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should raise an exception

    # Test case 3: Sequence list is longer
    header_list = ["Header1", "Header2"]
    sequence_list = ["ACGT", "GTCAGT", "AGT"]
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should raise an exception

    # Test case 4: Both lists are empty
    header_list = []
    sequence_list = []
    _verify_lists(header_list, sequence_list)  # Should not raise an exception

    # Test case 5: Header and sequence lists are both empty, but not of the same size
    header_list = ["Header1"]
    sequence_list = []
    with pytest.raises(SystemExit):
        _verify_lists(header_list, sequence_list)  # Should raise an exception


# Test cases for _get_num_nucleotides
def test_get_num_nucleotides():
    """
    testing the _get_num_nucleotides() function
    """

    # Test case 1: Basic test with all valid nucleotides
    sequence = "ACGT"
    assert _get_num_nucleotides('A', sequence) == 1
    assert _get_num_nucleotides('C', sequence) == 1
    assert _get_num_nucleotides('G', sequence) == 1
    assert _get_num_nucleotides('T', sequence) == 1

    # Test case 2: No occurrence of a nucleotide
    sequence = "CGCGCG"
    assert _get_num_nucleotides('A', sequence) == 0
    assert _get_num_nucleotides('T', sequence) == 0

    # Test case 3: Nucleotide count with mixed case
    sequence = "ACGtGtaNnN"
    assert _get_num_nucleotides('A', sequence) == 2
    assert _get_num_nucleotides('G', sequence) == 3
    assert _get_num_nucleotides('T', sequence) == 2
    assert _get_num_nucleotides('N', sequence) == 2

    # Test case 4: Invalid nucleotide
    sequence = "XCGT"
    with pytest.raises(SystemExit):
        _get_num_nucleotides('X', sequence)  # Should raise an exception

    # Test case 5: Empty sequence
    sequence = ""
    assert _get_num_nucleotides('A', sequence) == 0
    assert _get_num_nucleotides('T', sequence) == 0


# Test cases for _get_ncbi_accession
def test_get_ncbi_accession():
    """
    testing the _get_ncbi_accession() function
    """

    # Test case 1: Basic test with a valid NCBI header
    header = "NC_12345.1 Some description here"
    accession = _get_ncbi_accession(header)
    assert accession == "NC_12345.1"

    # Test case 2: Header with only the accession
    header = "NC_54321.2"
    accession = _get_ncbi_accession(header)
    assert accession == "NC_54321.2"

    # Test case 3: Header with extra spaces
    header = "  NC_67890.3  Description with spaces  "
    accession = _get_ncbi_accession(header)
    assert accession == "NC_67890.3"

    # Test case 4: Header without a valid accession, should raise an exception
    header = "Invalid header format"
    with pytest.raises(IndexError):
        _get_ncbi_accession(header)

    # Test case 5: Header with special characters
    header = "NC_1234.5$ Description with special characters"
    accession = _get_ncbi_accession(header)
    assert accession == "NC_1234.5"


# Test cases for calculate_gc_content
def test_calculate_gc_content():
    """
    testing the _calculate_gc_content() function
    """

    # Test case 1: Basic test with balanced GC content
    sequence = "GCGC"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 50.0

    # Test case 2: All adenine (A)
    sequence = "AAAA"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 0.0

    # Test case 3: All cytosine (C)
    sequence = "CCCC"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 100.0

    # Test case 4: All guanine (G)
    sequence = "GGGG"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 100.0

    # Test case 5: All thymine (T)
    sequence = "TTTT"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 0.0

    # Test case 6: Mix of nucleotides
    sequence = "ACGTACGT"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 50.0

    # Test case 7: Empty sequence
    sequence = ""
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 0.0

    # Test case 8: Sequence with special characters
    sequence = "GC!@CGCTT"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 55.6  # Rounded to one decimal place

    # Test case 9: Sequence with spaces
    sequence = "GC CG CTT"
    gc_percentage = calculate_gc_content(sequence)
    assert gc_percentage == 55.6  # Rounded to one decimal place


# Test cases for output_results_to_files
def test_output_results_to_files(tmp_path):
    """

    :param tmp_path:
    :return:
    """

    # Test case 1: Basic test with two sequences
    output_file = tmp_path / "output.txt"
    header_list = [">Seq1", ">Seq2"]
    sequence_list = ["AGCT", "GTCAGT"]
    output_results_to_files(header_list, sequence_list, output_file)

    with output_file.open() as outfile:
        lines = list(outfile)

    assert len(lines) == 3  # Including the header line
    assert lines[0] == "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n"
    assert lines[1] == "1\tSeq1\t1\t1\t1\t1\t0\t4\t50.0\n"
    assert lines[2] == "2\tSeq2\t2\t1\t1\t2\t0\t6\t33.3\n"

    # Test case 2: Multiple sequences, including empty sequences
    output_file = tmp_path / "output.txt"
    header_list = [">Seq1", ">Seq2", ">Seq3"]
    sequence_list = ["AGCT", "", "GTCAGT"]
    output_results_to_files(header_list, sequence_list, output_file)

    with output_file.open() as outfile:
        lines = list(outfile)

    assert len(lines) == 4  # Including the header line
    assert lines[0] == "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n"
    assert lines[1] == "1\tSeq1\t1\t1\t1\t1\t0\t4\t50.0\n"
    assert lines[2] == "3\tSeq3\t2\t1\t1\t2\t0\t6\t33.3\n"
    assert lines[3] == "2\tSeq2\t0\t0\t0\t0\t0\t0\t0.0\n"

    # Test case 3: No sequences
    output_file = tmp_path / "output.txt"
    header_list = []
    sequence_list = []
    output_results_to_files(header_list, sequence_list, output_file)

    with output_file.open() as outfile:
        lines = list(outfile)

    assert len(lines) == 1  # Only the header line
    assert lines[0] == "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n"


# Run the tests
if __name__ == "__main__":
    pytest.main()
