def minimum_bribes(q):
    result = 0
    for index, value in enumerate(q):
        if (value - index) > 3:
            result = 'Too chaotic'

    if result != 'Too chaotic':
        while True:
            for index, value in enumerate(q):
                if (index) < len(q)-1 and value > q[index + 1]:
                    q[index], q[index+1] = q[index+1], q[index]
                    result += 1

            q = q[:-1]

            if len(q) <= 0:
                break

    return result
