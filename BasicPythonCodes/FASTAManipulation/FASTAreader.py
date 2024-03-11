# Assigning default values to variables
current_sequence_name = "None"
current_sequence = []

# Opening the FASTA file selected by the user
file_name = input("Enter the name of your FASTA file: ")
fasta_file = open(file_name, 'r')


# Extracting the sequence name
for line in fasta_file:
    line = line.strip()
    if line.startswith(">"):
        current_sequence_name = line[1:]
    else:
        current_sequence.append(line)

# Finding the sequence length
current_sequence = "".join(current_sequence)
current_sequence_length = len(current_sequence)

# Printing the results
print(f"{current_sequence_name} {current_sequence_length}")
