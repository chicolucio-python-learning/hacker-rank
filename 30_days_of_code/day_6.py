def odd_even_index(string):
    return string[::2] + ' ' + string[1::2]


if __name__ == "__main__":
    number_strings = int(input())
    strings = []
    for _ in range(number_strings):
        strings.append(input())

    for string in strings:
        print(odd_even_index(string))
