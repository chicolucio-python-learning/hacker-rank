def repeated_string(s, n):
    """Returns the number of occurrences of 'a' in the prefix of length n in
    the infinitely repeating string s.

    Parameters
    ----------
    s : string
        a string to repeat
    n : integer
        the number of characters to consider

    Returns
    -------
    integer
        the number of letter a's in the first n letters of the infinite string
        created by repeating s infinitely many times
    """
    full_repeat, slice_pos = divmod(n, len(s))
    a_counter = s.count('a') * full_repeat + s[:slice_pos].count('a')
    return a_counter
