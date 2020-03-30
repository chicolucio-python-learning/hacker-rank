def rot_left(a, d):
    """Performs a left rotation operation on an array

    Parameters
    ----------
    a : array
        array of integers
    d : integer
        number of rotations

    Returns
    -------
    array
        updated array after d rotations
    """

    rotated_array = []
    first_neg_idx = -len(a)
    for i in range(len(a)):
        rotated_array.append(a[first_neg_idx + d + i])
    return rotated_array
