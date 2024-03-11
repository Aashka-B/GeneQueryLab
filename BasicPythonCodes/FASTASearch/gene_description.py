"""
File: gene_names_from_chr21.py
This program asks the user to enter a gene symbol and then prints the description
for that gene based on data from the input file.

Note: The program uses chr21_genes.txt as the default input file.

Sample command for executing the program:

    python3 gene_description.py [-h] -i chr21_genes.txt
    OR
    python3 gene_description.py
"""
import argparse
# Importing the get_filehandle function
from FASTASearch.io_utils import get_filehandle


def read_gene_data(infile):
    """
    Reads gene data from the given file and
    returns a dictionary mapping gene symbols to descriptions.

    :param infile: Path to the input file containing gene data.
    :type infile: str
    :return: A dictionary mapping gene symbols to descriptions.
    :rtype: dict
    """
    gene_dict = {}

    # Using get_filehandle from io_utils to open files
    fh_in = get_filehandle(infile, 'r')
    for line in fh_in:
        parts = line.strip().split('\t')
        gene_dict[parts[0].upper()] = parts[1]
    return gene_dict


def get_cli_args():
    """
    Parse command line arguments using argparse.

    :return: An argparse.Namespace object containing the parsed arguments.
    :rtype: argparse.Namespace
    """

    # Define command-line arguments
    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt, and ask the user for a gene name')
    parser.add_argument('-i', '--infile', type=str,
                        default='chr21_genes.txt', help='Path to the file to open')
    return parser.parse_args()


def main():
    """Business logic"""

    args = get_cli_args()

    # Read gene data from the input file
    gene_data = read_gene_data(args.infile)

    # Ensuring case-insensitive user interaction and gene symbol validity
    while True:
        user_input = input('Enter gene name of interest. Type quit to exit: ').strip().upper()

        if user_input in gene_data:
            result = f'{user_input} found! Here is the description:\n{gene_data[user_input]}\n'
            print(result)
        elif user_input not in {'QUIT', 'EXIT'}:
            result = 'Not a valid gene name.\n'
            print(result)
        else:
            print('Thanks for querying the data.')
            break  # Exit the loop if user_input is 'QUIT' or 'EXIT'


if __name__ == '__main__':
    main()
