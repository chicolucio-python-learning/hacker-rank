from day_19 import AdvancedArithmetic, Calculator
import pytest


def test_AdvancedArithmetic_error():
    _ = AdvancedArithmetic()
    with pytest.raises(NotImplementedError):
        _.divisorSum()


def test_Calculator_divisors():
    _ = Calculator()
    assert _.divisors(6) == [1, 2, 3, 6]
    assert _.divisors(20) == [1, 2, 4, 5, 10, 20]


def test_Calculator_divisorSum():
    _ = Calculator()
    assert _.divisorSum(6) == 12
    assert _.divisorSum(20) == 42
