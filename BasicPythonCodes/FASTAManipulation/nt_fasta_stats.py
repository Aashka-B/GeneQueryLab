"""
File: nt_fasta_stats.py
This program generates nucleotide statistics for sequences in a FASTA file.

Sample command for executing the program:

python3 secondary_structure_splitter.py [-h] -i input_file.fasta -o output_file.txt
OR
python3 secondary_structure_splitter.py [--help] --infile input_file.fasta -outfile output_file.txt
"""
import argparse
import sys


def get_filehandle(file_name, mode):
    """

    :param file_name:
    :param mode:
    :return:
    """

    try:
        fh_in = open(file_name, mode, encoding="utf-8")
        return fh_in
    except OSError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)


def get_fasta_lists(fh_in):
    """

    :param fh_in:
    :return:
    """

    # Initializing variables
    header_list = []
    sequence_list = []
    current_sequence = ""

    for line in fh_in:
        line = line.strip()  # Remove leading/trailing whitespaces
        if not line:
            continue  # Skip empty lines

        if line[0] == ">":
            header_list.append(line[1:])  # Remove the ">" character
            if current_sequence:
                sequence_list.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line

    if current_sequence:
        sequence_list.append(current_sequence)

    _verify_lists(header_list, sequence_list)

    return header_list, sequence_list


def _verify_lists(header_list, sequence_list):
    """

    :param header_list:
    :param sequence_list:
    :return:
    """

    if len(header_list) != len(sequence_list):
        print("Header and Sequence lists size are different in size")
        print("Did you provide a FASTA formatted file?")
        sys.exit(1)


def _get_num_nucleotides(nucleotide, sequence):
    """

    :param nucleotide:
    :param sequence:
    :return:
    """

    valid_nt = "AGCTN"
    if nucleotide not in valid_nt:
        sys.exit("Did not code this condition")

    return sequence.count(nucleotide)


# Function to extract the accession number from the header
def _get_ncbi_accession(header):
    """

    :param header:
    :return:
    """

    header_components = header.split()
    accession = header_components[0]
    return accession


# Function to calculate GC content
def calculate_gc_content(sequence):
    """

    :param sequence:
    :return:
    """

    gc_count = sequence.count('G') + sequence.count('C')
    if len(sequence) > 0:
        gc_content = (gc_count / len(sequence)) * 100
    else:
        gc_content = 0
    return gc_content


# Function to output results to the specified file
def output_results_to_files(header_list, sequence_list, output_file):
    """

    :param header_list:
    :param sequence_list:
    :param output_file:
    :return:
    """

    print("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%", file=output_file)

    for i, (header, sequence) in enumerate(zip(header_list, sequence_list), start=1):
        accession = _get_ncbi_accession(header)
        a_nt_count = _get_num_nucleotides('A', sequence)
        g_nt_count = _get_num_nucleotides('G', sequence)
        c_nt_count = _get_num_nucleotides('C', sequence)
        t_nt_count = _get_num_nucleotides('T', sequence)
        n_nt_count = _get_num_nucleotides('N', sequence)
        sequence_length = len(sequence)
        gc_percentage = calculate_gc_content(sequence)

        print(f"{i}"
              f"\t{accession}"
              f"\t{a_nt_count}"
              f"\t{g_nt_count}"
              f"\t{c_nt_count}"
              f"\t{t_nt_count}"
              f"\t{n_nt_count}"
              f"\t{sequence_length}"
              f"\t{gc_percentage:.1f}",
              file=output_file)


def get_cli_args():
    """
        void: get_cli_args()
        Takes: no arguments
        @return: instances of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description="Provide a FASTA file to generate nucleotide statistics")
    parser.add_argument("-i", "--infile", required=True, type=str, help="Path to file to open")
    parser.add_argument("-o", "--outfile", required=True, type=str, help="Path to file to write")
    return parser.parse_args()


def main():
    """Business logic"""

    args = get_cli_args()

    # Using get_filehandle() for one input file and one output file
    infile = get_filehandle(args.infile, "r")
    outfile = get_filehandle(args.outfile, "w")

    # Get the two lists of data from the input FASTA file
    header_list, sequence_list = get_fasta_lists(infile)

    # Print out results and get some output variables
    output_results_to_files(header_list, sequence_list, outfile)

    # Closing files
    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
