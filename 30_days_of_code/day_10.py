# it could be directly converted to string, but I wanted to use a list to learn
# the insert method


def dec_to_bin(number):
    n = number
    bin_digits = []
    while n > 0:
        remainder = divmod(n, 2)[1]
        n = divmod(n, 2)[0]
        bin_digits.insert(0, remainder)

    return bin_digits


def list_to_string(lst):
    return ''.join([str(i) for i in lst])


def count1(bin_str):
    flag = True
    bin_str_len = len(bin_str)
    count = 0

    while flag:
        flag = False
        for i in range(bin_str_len, 0, -1):
            if '1'*i in bin_str:
                count = i
                break
    return count


def main(number):
    lst = dec_to_bin(number)
    string = list_to_string(lst)
    return count1(string)


if __name__ == "__main__":
    n = int(input())
    print(main(n))
