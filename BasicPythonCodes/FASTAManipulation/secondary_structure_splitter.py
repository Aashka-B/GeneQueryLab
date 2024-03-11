"""
File: secondary_structure_splitter.py
A program to split a combined FASTA file into protein sequences and secondary structures
and generate respective output files.

Sample command for executing the program:

python3 secondary_structure_splitter.py [-h] -i input_file.fasta
OR
python3 secondary_structure_splitter.py [--help] --infile input_file.fasta
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
        line = line.strip()  # Remove leading/trailing whitespace
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


def output_results_to_files(header_list, sequence_list, fh_out1, fh_out2):
    """

    :param header_list:
    :param sequence_list:
    :param fh_out1:
    :param fh_out2:
    :return:
    """

    num_proteins = len(header_list)
    num_ss = len(sequence_list)

    for header, sequence in zip(header_list, sequence_list):
        if sequence.isalpha():
            fh_out1.write(header)
            fh_out1.write(sequence + "\n")
        else:
            fh_out2.write(header)
            # Write the secondary structure sequence with line breaks preserved
            for line in sequence.splitlines():
                fh_out2.write(line + "\n")

    return num_proteins, num_ss


def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arguments
    @return: instances of argparse arguments
    """

    parser = argparse.ArgumentParser(
        description="Provide a FASTA file to perform splitting on sequence and secondary structure")
    parser.add_argument("-i", "--infile", required=True, type=str, help="Path to file to open")
    return parser.parse_args()


def main():
    """Business logic"""

    args = get_cli_args()
    infile = args.infile

    # Hard-coded the pdb_protein.fasta and pdb_ss.fasta file names into the program
    outfile1 = "pdb_protein.fasta"
    outfile2 = "pdb_ss.fasta"

    # Using get_filehandle() for one input file and two output files
    fh_in = get_filehandle(infile, 'r')
    fh_out1 = get_filehandle(outfile1, 'w')
    fh_out2 = get_filehandle(outfile2, 'w')

    # Get the two lists of data from the input FASTA file
    header_list, sequence_list = get_fasta_lists(fh_in)

    # Print out results and get some output variables
    num_proteins, num_ss = output_results_to_files(header_list, sequence_list, fh_out1, fh_out2)

    # Writing to stderr
    sys.stderr.write(f"Found {num_proteins} protein sequences\n")
    sys.stderr.write(f"Found {num_ss} ss sequences\n")

    # Closing files
    fh_in.close()
    fh_out1.close()
    fh_out2.close()


if __name__ == "__main__":
    main()
