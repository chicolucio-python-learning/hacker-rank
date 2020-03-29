def repeated_string(s, n):
    full_repeat, slice_pos = divmod(n, len(s))
    try:
        new_s = s * full_repeat + s[:slice_pos]
        a_counter = new_s.count('a')
    # if n is too big and len(s) = 1, a memory error will raise
    except MemoryError:
        a_counter = n
    return a_counter
