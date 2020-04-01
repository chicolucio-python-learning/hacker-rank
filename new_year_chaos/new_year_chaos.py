def minimum_bribes(q):
    """Returns the minimum number of bribes necessary, or Too chaotic if the
    line configuration is not possible

    Parameters
    ----------
    q : array
        An array of integers

    Returns
    -------
    integer or string
        The minimum number of bribes necessary or 'Too chaotic'
    """
    result = 0
    for index, value in enumerate(q):
        if (value - index) > 3:
            result = 'Too chaotic'

    if result != 'Too chaotic':
        swap_flag = True  # flag if swaps happened in previous iteration
        while swap_flag:
            swap_flag = False
            for index, value in enumerate(q):
                if (index) < len(q)-1 and value > q[index + 1]:
                    q[index], q[index+1] = q[index+1], q[index]
                    result += 1
                    swap_flag = True

            q = q[:-1]

            if len(q) <= 0:
                break

    return result
