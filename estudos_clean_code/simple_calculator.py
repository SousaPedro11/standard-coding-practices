from decorators import operations


class SimpleCalculator:
    @operations
    def add(self, number_1: float, number_2: float) -> float:
        return number_1 + number_2

    @operations
    def subtract(self, number_1: float, number_2: float) -> float:
        return number_1 - number_2

    @operations
    def divide(self, number_1: float, number_2: float) -> float:
        return number_1 / number_2

    @operations
    def multiply(self, number_1: float, number_2: float) -> float:
        return number_1 * number_2
