def jumping_clouds(c):
    """Determines the minimum number of jumps from start position to the last
    cloud

    Parameters
    ----------
    c : list
        array of binary integers

    Returns
    -------
    integer
        minimum number of jumps
    """
    forbidden_clouds_idx = [i for i, x in enumerate(c) if x == 1]
    max_idx = len(c) - 1
    min_jumps = 0
    aux = 0

    while aux != max_idx:
        if (aux + 2) not in forbidden_clouds_idx and (aux + 2) <= max_idx:
            aux += 2
            min_jumps += 1
        else:
            aux += 1
            min_jumps += 1
    return min_jumps
