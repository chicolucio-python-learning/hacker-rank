def bubble_sort(array):
    numSwaps = 0
    for _ in range(len(array)):
        aux = 0

        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                numSwaps += 1
                aux += 1

        if aux == 0:
            break

    return numSwaps, array
