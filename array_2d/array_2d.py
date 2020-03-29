def hourglass_sum(arr):
    """Return the maximum hourglass sum in a given array

    Parameters
    ----------
    arr : array
        an array of integers

    Returns
    -------
    integer
        The maximum hourglass sum in a given array
    """
    sum_pattern = []
    for line in range(len(arr) - 2):
        aux = 0
        for column in range(len(arr[line]) - 2):
            aux_same_line = arr[line][column] + \
                arr[line][column + 1] + arr[line][column + 2]
            aux_line_down = arr[line+1][column + 1]
            aux_two_lines_down = arr[line + 2][column] + \
                arr[line + 2][column + 1] + arr[line + 2][column + 2]
            aux = aux_same_line + aux_line_down + aux_two_lines_down
            sum_pattern.append(aux)
    return max(sum_pattern)
