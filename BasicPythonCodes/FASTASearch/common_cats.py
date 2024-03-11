"""
File: common_cats.py
This program counts how many genes are in each category (1.1, 1.2, 2.1 etc.)
based on data from the input gene file and the input gene category description file.

Note: The program uses chr21_genes.txt and chr21_genes_categories.txt
        as the default input files.

Sample command for executing the program:

    python3 find_common_cats.py [-h] -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
    OR
    python3 find_common_cats.py
"""
import argparse
# Importing the get_filehandle function
from FASTASearch.io_utils import get_filehandle


# Function to read category descriptions from chr21_gene_categories.txt
def read_category_descriptions(filename):
    """
    Reads category descriptions from the specified file and returns
    a dictionary mapping category codes to descriptions.

    :param filename: Path to the input file containing category descriptions.
    :type filename: str
    :return: A dictionary mapping category codes to descriptions.
    :rtype: dict
    """

    category_descriptions = {}
    fh_in = get_filehandle(filename, 'r')
    for line in fh_in:
        line = line.strip()
        if line:
            category, description = line.split(None, 1)
            category_descriptions[category] = description
    return category_descriptions


# Function to count genes in each category
def count_genes_by_category(genes_filename, categories_filename, output_filename):
    """
    Counts the number of genes in each category based on data from the input gene file
    and the input gene category description file. Writes the results to the output file.

    :param genes_filename: Path to the gene description file.
    :type genes_filename: str
    :param categories_filename: Path to the gene category file.
    :type categories_filename: str
    :param output_filename: Path to the output file to write results.
    :type output_filename: str
    """

    # Read category descriptions
    category_descriptions = read_category_descriptions(categories_filename)

    # Initialize category counts
    category_counts = {category: 0 for category in category_descriptions}

    # Read genes and count by category
    gene_file = get_filehandle(genes_filename, 'r')
    for line in gene_file:
        line = line.strip()
        if line:
            gene_category = line.split('\t')[-1]  # Assuming category is the last column
            if gene_category in category_counts:
                category_counts[gene_category] += 1

    # Write results to output file
    outfile = get_filehandle(output_filename, 'w')
    outfile.write("   Category\tOccurrence\tDescription\n")
    # Sort categories based on their numerical value
    sorted_categories = sorted(category_counts.keys())
    for category in sorted_categories:
        outfile.write(
            f"{category}\t{category_counts[category]}\t{category_descriptions[category]}\n")


def get_cli_args():
    """
    Parse command-line arguments using argparse.

    :return: An argparse.Namespace object containing the parsed arguments.
    :rtype: argparse.Namespace
    """

    # Define command-line arguments
    parser = argparse.ArgumentParser(
        description="Combine on gene name and count the category occurrence")
    parser.add_argument("-i1", "--infile1", type=str,
                        default="chr21_genes.txt", help="Path to the gene description file to open")
    parser.add_argument("-i2", "--infile2", type=str,
                        default="chr21_genes_categories.txt", help="Path to the gene category file to open")
    return parser.parse_args()


def main():
    """Business logic"""

    # Parse command-line arguments
    args = get_cli_args()

    # Output filename
    output_filename = 'OUTPUT/categories.txt'

    # Count genes by category and write results to the output file
    count_genes_by_category(args.infile1, args.infile2, output_filename)


if __name__ == '__main__':
    main()
