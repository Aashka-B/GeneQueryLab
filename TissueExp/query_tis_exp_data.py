"""
File: query_tis_exp_data.py

This program allows bioinformaticians to query the tissue expression data
from a Unigene file for a given gene and species.

Usage:
python query_tis_exp_data.py [-h] --host HoSt_nAMe --gene GENE_NAME
"""
# Importing necessary modules
import argparse
import re
import sys
import os

from TissueExp import config
from TissueExp import io_utils


# Defining functions
def update_host_name(host_name: str) -> str:
    """
    Updates the host name to its scientific name.
    """

    host_keywords = config.get_keywords_for_hosts()
    host_name_lower = host_name.lower().replace('_', ' ')

    for key, value in host_keywords.items():
        if host_name_lower == key.lower():
            return value

    _print_directories_for_hosts()
    sys.exit(1)


def _print_directories_for_hosts():
    """
    Prints available host directories if the specified directory is not found.
    """
    host_keywords = config.get_keywords_for_hosts()

    scientific_names = sorted(set(scientific_name for common_name, scientific_name in host_keywords.items()))
    common_names = sorted(set(common_name for common_name, scientific_name in host_keywords.items()))

    print("\nEither the Host Name you are searching for is not in the database")
    print("\nor If you are trying to use the scientific name please put the name in double quotes:\n")
    print("\"Scientific name\"\n")
    print("Here is a (non-case sensitive) list of available Hosts by scientific name\n")

    max_index_width_1 = len(str(len(scientific_names)))

    for index, scientific_name in enumerate(scientific_names, start=1):
        formatted_index = f"{index:>{max_index_width_1}}."
        print(f"  {formatted_index} {scientific_name}")

    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")

    max_index_width_2 = len(str(len(common_names)))

    for index, common_name in enumerate(common_names, start=1):
        formatted_index = f"{index:>{max_index_width_2}}."
        print(f"  {formatted_index} {common_name}")


def get_data_for_gene_file(gene_file_name: str) -> list:
    """
    Opens the gene file, extracts tissue expression data, and returns a sorted list of tissues.
    """
    tissues = []
    with io_utils.get_filehandle(gene_file_name, 'r') as file:
        for line in file:
            match = re.search(r"EXPRESS (.+)", line)
            if match:
                tissues_string = match.group(1)
                tissues = tissues_string.split('|')

    # Strip whitespace from each tissue and sort the list
    tissues = sorted(tissue.strip() for tissue in tissues)

    return tissues


def print_host_to_gene_name_output(host_name: str, gene_name: str, tissues: list):
    """
    Prints tissue expression data for the gene.
    """
    print(f"\nFound Gene {gene_name} for {host_name}")
    print(f"In {host_name}, There are {len(tissues)} tissues that {gene_name} is expressed in:\n")

    max_index_width_3 = len(str(len(tissues)))

    for index, tissue in enumerate(tissues, start=1):
        formatted_index = f"{index:>{max_index_width_3}}."
        formatted_tissue = ' '.join(word.capitalize() if i == 0 else word.lower()
                                    for i, word in enumerate(tissue.split()))
        print(f" {formatted_index} {formatted_tissue}")


def get_cli_args():
    """
    Parse command-line arguments using argparse.

    :return: An argparse.Namespace object containing the parsed arguments.
    :rtype: argparse.Namespace
    """

    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Get tissue expression data for a given gene and host.")
    parser.add_argument("--host", default="Homo sapiens", type=str, help="Name of Host")
    parser.add_argument("-g", "--gene", default="TGM1", type=str, help="Name of Gene")
    return parser.parse_args()


def main():
    """Business logic"""

    # Parse command-line arguments
    args = get_cli_args()

    host_name = args.host
    gene_name = args.gene

    host_name = update_host_name(host_name)
    gene_file_path = os.path.join(config.get_directory_for_unigene(), host_name,
                                  gene_name + "." + config.get_extension_for_unigene())

    if io_utils.is_gene_file_valid(gene_file_path):
        tissues = get_data_for_gene_file(gene_file_path)
        print_host_to_gene_name_output(host_name, gene_name, tissues)
    else:
        print("Not found")
        print(f"Gene {gene_name} does not exist for {host_name}. Exiting now...", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
