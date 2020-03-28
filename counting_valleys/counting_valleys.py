def counting_valleys(n, s):
    """Calculates the number of valleys

    Parameters
    ----------
    n : int
        number of steps
    s : str
        string describing path

    Returns
    -------
    int
        number of valleys
    """
    altitude_before_move = 0
    altitude_after_move = 0
    valleys = 0

    for char in s:
        if char == 'D':
            altitude_after_move = altitude_before_move - 1
        if char == 'U':
            altitude_after_move = altitude_before_move + 1

        if altitude_before_move == 0 and altitude_after_move < 0:
            valleys += 1

        altitude_before_move = altitude_after_move

    return valleys
