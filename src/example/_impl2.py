def sum_two_list(l1, l2):
    """This function sums two lists element-wise.
    If the lists are of different lengths, it will sum up to the length of the shorter list.
    """
    return [x + y for x, y in zip(l1, l2, strict=True)]