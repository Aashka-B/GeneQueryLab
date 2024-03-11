"""Calculating average molecular weight of a selected protein
based on the length of the DNA sequence of the gene encoding for the selected protein"""

import sys

# Prompting the user to provide a name for the DNA sequence
GENE_NAME = input("\nPlease enter a name for the DNA sequence: ")
print("Your sequence name is:", GENE_NAME)

# Prompting the user to provide the length of the sequence
SEQUENCE_LENGTH = input("Please enter the length of the sequence: ")

# Converting input type to float
SEQUENCE_LENGTH = float(SEQUENCE_LENGTH)

# Checking if the input is divisible by 3, AND
# Exiting a program in Python using sys.exit() in case of an error
if SEQUENCE_LENGTH % 3 != 0:
    # print to STDERR
    print("\n\nError: the DNA sequence is not a multiple of 3\n", file=sys.stderr)
    # Assigning a non-zero exit value, since zero is considered "successful termination"
    sys.exit(1)

else:
    # Printing the sequence
    print("The length of the DNA sequence is:", SEQUENCE_LENGTH)

    # Calculating the number of amino acids
    NUM_AMINO_ACIDS = SEQUENCE_LENGTH // 3
    print("The length of the decoded protein is:", NUM_AMINO_ACIDS)

    # Average molecular weight of an amino acid in daltons
    AVG_MOL_WT_PER_AA = 110

    # Calculating the estimated molecular weight of the resulting protein in kilodaltons
    PROTEIN_MOL_WT = (NUM_AMINO_ACIDS * 110) / 1000
    print("The average weight of the protein sequence is:", PROTEIN_MOL_WT)
print("\r")
