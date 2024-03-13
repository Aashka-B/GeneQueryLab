"""
File: common_genes.py
This program finds all gene symbols that appear in both the input gene files.

Note: The program uses chr21_genes.txt and HUGO_genes.txt
        as the default input files.

Sample command for executing the program:

    python3 common_genes.py [-h] -i1 chr21_genes.txt -i2 HUGO_genes.txt
    OR
    python3 common_genes.py
"""
import argparse
# Importing the get_filehandle function
from FASTASearch.io_utils import get_filehandle


def read_gene_symbols(filename):
    """
    Reads gene symbols from the specified file and returns a set of unique gene symbols.

    :param filename: Path to the input file containing gene symbols.
    :type filename: str
    :return: A set of unique gene symbols.
    :rtype: set
    """

    gene_symbols = set()
    with get_filehandle(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            gene_symbol = line.strip().split(None, 1)[0]
            gene_symbols.add(gene_symbol)
    return gene_symbols


def find_intersection(infile1, infile2, output_filename):
    """
    Finds the intersection of gene symbols between two input files
    and writes the result to an output file.

    :param infile1: Path to the first input file containing gene symbols.
    :type infile1: str
    :param infile2: Path to the second input file containing gene symbols.
    :type infile2: str
    :param output_filename: Path to the output file to write common gene symbols.
    :type output_filename: str
    :return: The number of common gene symbols found.
    :rtype: int
    """

    gene_symbols_1 = read_gene_symbols(infile1)
    gene_symbols_2 = read_gene_symbols(infile2)

    common_symbols = gene_symbols_1.intersection(gene_symbols_2)

    with get_filehandle(output_filename, 'w') as outfile:
        for symbol in sorted(common_symbols):
            outfile.write(f"{symbol}\n")

    return len(common_symbols)


def get_cli_args():
    """
    Parse command-line arguments using argparse.

    :return: An argparse.Namespace object containing the parsed arguments.
    :rtype: argparse.Namespace
    """

    # Define command-line arguments
    parser = argparse.ArgumentParser(
        description="Provide two gene lists (ignore header line), find intersection")
    parser.add_argument("-i1", "--infile1", help="Gene list 1 to open",
                        default="chr21_genes.txt")
    parser.add_argument("-i2", "--infile2", help="Gene list 2 to open",
                        default="HUGO_genes.txt")
    return parser.parse_args()


def main():
    """Business logic"""

    # Parse command-line arguments
    args = get_cli_args()

    # Output filename
    output_filename = 'OUTPUT/intersection_output.txt'

    # Count unique gene symbols in each input file
    gene_count_1 = len(read_gene_symbols(args.infile1))
    gene_count_2 = len(read_gene_symbols(args.infile2))

    # Find and write the intersection of gene symbols
    common_count = find_intersection(args.infile1, args.infile2, output_filename)

    # Print summary information
    print(f"Number of unique gene names in {args.infile1}: {gene_count_1}")
    print(f"Number of unique gene names in {args.infile2}: {gene_count_2}")
    print(f"Number of common gene symbols found: {common_count}")
    print(f"Output stored in {output_filename}")


if __name__ == '__main__':
    main()
