"""Calculating the estimated molecular weight of a protein (in kilodaltons)"""

# Hard-coded protein sequence for Rattus norvegicus PKC Beta-1
PROTEIN_SEQUENCE = ("MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC"
                    "CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH"
                    "KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ"
                    "KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ"
                    "EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK"
                    "GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM"
                    "EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE"
                    "NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY"
                    "PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF"
                    "DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV")

# Getting rid of newline characters
PROTEIN_SEQUENCE = PROTEIN_SEQUENCE.replace('\r', '').replace('\n', '')

# Printing the length of the protein sequence
print('\nThe length of "Protein kinase C beta type" is:', len(PROTEIN_SEQUENCE))

# Average molecular weight of an amino acid in Daltons (AVG_MOL_WT_PER_AA)
AVG_MOL_WT_PER_AA = 110

# Calculating the molecular weight of the protein (PROTEIN_MOL_WT) in Daltons
PROTEIN_MOL_WT = len(PROTEIN_SEQUENCE) * AVG_MOL_WT_PER_AA

# Converting the molecular weight from daltons to kilodaltons
PROTEIN_MOL_WT_KD = PROTEIN_MOL_WT / 1000

# Obtaining the result
print("The average weight of this protein sequence in kilodaltons is:", PROTEIN_MOL_WT_KD)
print("\r")
