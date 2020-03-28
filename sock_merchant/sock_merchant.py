def sock_merchant(n, ar):
    """Returns an integer representing the number of matching pairs of socks

    Parameters
    ----------
    n : int
        number of socks in the pile
    ar : list
        the colors of each sock (represented by integers)

    Returns
    -------
    int
        number of matching pairs
    """
    unique = set(ar)  # gets unique values (colors)
    count_per_unique = [ar.count(i) for i in unique]  # socks per color
    pair = [i//2 if i >= 2 else 0 for i in count_per_unique]  # pairs per color
    return sum(pair)
