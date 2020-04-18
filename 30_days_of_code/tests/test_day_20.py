from day_20 import bubble_sort


def test_bubble_sort_case0():
    test_case0 = [1, 2, 3]
    assert bubble_sort(test_case0)[0] == 0
    assert bubble_sort(test_case0)[1] == [1, 2, 3]


def test_bubble_sort_case1():
    test_case1 = [3, 2, 1]
    assert bubble_sort(test_case1)[0] == 3
    assert bubble_sort(test_case1)[1] == [1, 2, 3]
