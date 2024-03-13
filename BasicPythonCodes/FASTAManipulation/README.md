# FASTAManipulation

Welcome to the FASTAManipulation folder of the GeneQueryLab repository, where we provide a collection of Python scripts designed for the efficient handling, analysis, and manipulation of FASTA and Unigene files. This suite of tools is developed to assist bioinformaticians, geneticists, and data scientists in extracting meaningful insights from genetic sequences with ease and precision.

## Contents

- **FASTAreader.py**: A script for reading FASTA files and extracting sequence information. It demonstrates how to parse FASTA files to extract names and sequences, calculating sequence lengths along the way.

- **nt_fasta_stats.py**: Generates comprehensive nucleotide statistics for sequences contained in FASTA files. This script is essential for obtaining a detailed nucleotide composition analysis, including counts of each nucleotide and GC content.

- **sec_structure_split.py**: Splits combined FASTA files into separate files for protein sequences and their corresponding secondary structures. This utility is crucial for researchers focusing on protein structure analysis.

- **test_nt_fasta_stats.py** and **test_sec_structure_split.py**: Contain unit tests for validating the functionality of `nt_fasta_stats.py` and `sec_structure_split.py`, respectively, ensuring reliability and accuracy of the scripts.

- **run_lints.sh**: A shell script to run linting tools (e.g., Pylint, Flake8) against the Python scripts to ensure code quality and adherence to Python coding standards.

## Getting Started

To use these scripts, clone the GeneQueryLab repository and navigate to the FASTAManipulation folder. Ensure you have Python 3.x installed on your system, along with necessary packages (e.g., `argparse`, `pytest` for running tests).

## Usage

Each script is designed to be run from the command line. Here's an example to run `FASTAreader.py`:

```bash
python FASTAreader.py
