import math


class Calculator:
    def __init__(self) -> None:
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result

    def sub(self, a, b):
        result = a - b
        self.history.append(result)
        return result

    def mul(self, a, b):
        result = a * b
        self.history.append(result)
        return result

    def div(self, a, b):
        result = a / b
        self.history.append(result)
        return result

    def sqrt(self, a):
        result = math.sqrt(a)
        self.history.append(result)
        return result
