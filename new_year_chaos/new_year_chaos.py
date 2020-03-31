def minimum_bribes(q):
    result = 0
    moves = []

    for i in range(len(q), 0, -1):
        if q[i-1] == i:
            pass
        elif q[i-1] - i > 2:
            result = 'Too chaotic'
            break
        elif q[i-1] - i < 0:
            pass
        else:
            moves.append((q[i-1], q[i-1] - i))

    if result != 'Too chaotic':
        result = sum([moves[i][1] for i in range(len(moves))])
        # for i in range(len(moves)-1):
        #     if (moves[i][1] == 2) and (moves[i+1][1] == 2) and (moves[i][0] == moves[i+1][0] + 1):
        #         result += 1
        count_1_2 = [moves[i][1] for i in range(len(moves))]
        result += count_1_2.count(2)//3

    return result
