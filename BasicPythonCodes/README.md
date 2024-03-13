# BasicPythonCodes

The BasicPythonCodes directory within the GeneQueryLab repository is a collection of fundamental Python scripts that showcase basic bioinformatics calculations and data analysis techniques. These scripts are designed to provide a solid foundation in bioinformatics programming, covering essential operations such as sequence manipulation, molecular weight calculations, and statistical analysis.

## Contents

- **basic_stats.py**: Calculates descriptive statistics for numbers found in columns of a given input file, including average, maximum, minimum, variance, standard deviation, and median.

- **calc_kda.py**: Estimates the molecular weight of a protein (in kilodaltons) based on its amino acid sequence. The script demonstrates handling and processing of a hardcoded protein sequence.

- **calc_prot_mol_wt.py**: Calculates the average molecular weight of a protein based on the length of the DNA sequence of the gene encoding the protein. This script prompts users for input and handles basic error checking.

- **rev_comp.py**: Generates the reverse complement of a given DNA sequence, showcasing sequence manipulation techniques fundamental to bioinformatics.

## Getting Started

To use these scripts, clone the GeneQueryLab repository and navigate to the BasicPythonCodes folder. Ensure Python 3.x is installed on your system.

```bash
git clone https://github.com/yourusername/GeneQueryLab.git
cd GeneQueryLab/BasicPythonCodes
```

## Usage
Scripts can be run from the command line. For instance, to calculate basic statistics from a file:
```bash
python basic_stats.py input_file.txt column_number
```
Replace input_file.txt with the path to your data file and column_number with the column index (starting from 0) you want to analyze.

## Prerequisites
These scripts require Python 3.x. No additional libraries are needed for rev_comp.py, calc_kda.py, and calc_prot_mol_wt.py. The basic_stats.py script may require you to have specific data files ready for analysis.
