def str_to_int(string):
    try:
        i = int(string)
    except ValueError:
        i = 'Bad String'
    return i


if __name__ == "__main__":
    S = input().strip()
    print(str_to_int(S))
