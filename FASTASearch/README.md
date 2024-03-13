# FASTASearch

The FASTASearch folder within the GeneQueryLab repository encompasses a suite of tools and resources designed for bioinformatics analyses focusing on gene identification and categorization based on FASTA file data. This repository aims to assist in the exploration and understanding of genetic sequences, facilitating research in genomics and related fields.

## Contents

This directory contains the following files and subdirectories for module-specific utilities and testing:

- **chr21_genes_categories.txt**: Categorization of genes from chromosome 21 based on their identity and functional association.
- **chr21_genes.txt**: List of genes from chromosome 21, including descriptions and category classifications.
- **HUGO_genes.txt**: A comprehensive list of genes from the HUGO Gene Nomenclature Committee, featuring gene symbols and descriptions.
- **common_gene_cats.py**: A Python script to count the number of genes in each category based on chr21_genes_categories.txt and chr21_genes.txt.
- **common_genes.py**: This script identifies common gene symbols between chr21_genes.txt and HUGO_genes.txt.
- **gene_description.py**: A utility for printing the description of a gene symbol entered by the user, using data from chr21_genes.txt.

### FASTASearch Module

The FASTASearch subdirectory/module contains utilities for file handling and I/O operations essential for the main scripts:

- **__init__.py**: Marks the directory as a Python package.
- **io_utils.py**: Includes functions for processing command line user input files and facilitating file I/O operations.

## Getting Started

To utilize these tools, clone the GeneQueryLab repository and navigate to the FASTASearch folder. Ensure you have Python 3.x installed on your system, along with necessary packages (e.g., `argparse`, `pytest` for running tests).

## Usage

Each script is designed to be run from the command line. For example, to use gene_description.py:

```bash
python gene_description.py -i chr21_genes.txt
