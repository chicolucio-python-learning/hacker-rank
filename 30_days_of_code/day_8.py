if __name__ == "__main__":

    phone_book = dict()

    num_entries = int(input())

    for _ in range(num_entries):
        entry = input().rstrip().split()
        phone_book[entry[0]] = entry[1]
        entry = None

    while True:
        try:
            look_up = input()
            if phone_book.get(look_up) == None:
                print('Not found')
            else:
                print(look_up + '=' + phone_book.get(look_up))
        except:
            break
