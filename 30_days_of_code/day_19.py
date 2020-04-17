class AdvancedArithmetic():
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisors(self, n):
        div = []
        for _ in range(1, n+1):
            if n % _ == 0:
                div.append(_)
        return div

    def divisorSum(self, n):
        return sum(self.divisors(n))


if __name__ == "__main__":
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)
