from day_14 import Difference

lst_sample_test_case0 = [1, 2, 5]
lst_sample_test_case1 = [8, 19, 3, 2, 7]
lst_sample_test_case2 = [8, 8, 8, 8, 8]


def test_case0():
    test = Difference(lst_sample_test_case0)
    assert test.maximumDifference == 4


def test_case1():
    test = Difference(lst_sample_test_case1)
    assert test.maximumDifference == 17


def test_case2():
    test = Difference(lst_sample_test_case2)
    assert test.maximumDifference == 0
