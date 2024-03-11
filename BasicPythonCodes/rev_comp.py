def rev_comp(seq):
    """
    :param:
    :return:
    """
    # Define compliment dictionary
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement = [complement_dict[base] for base in reversed(seq)]
    return ''.join(reverse_complement)
