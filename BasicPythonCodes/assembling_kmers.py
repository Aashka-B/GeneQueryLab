def assemble_kmers(kmer1, kmer2):
    # Defining max possible overlap
    overlap = len(kmer1)
    assembly = kmer2 + kmer1[:overlap]
    print(f"Assembly: {assembly}")
    print(max_overlap)


def main():
    # Getting input kmer sequences
    kmer1 = input("Insert kmer1 sequence")
    kmer2 = input("Insert kmer2 sequence")

    # Checking if the length of the kmers are same
    if len(kmer1) != len(kmer2):
        assert "kmers must be same length"
    else:
        assemble_kmers(kmer1, kmer2)


if __name__ == "__main__":
    main()
