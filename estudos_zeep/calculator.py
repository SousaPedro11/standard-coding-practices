from abc import abstractmethod, ABC

import attr
from zeep.client import Client


@attr.s(auto_attribs=True)
class Calculator(ABC):
    num1: int = False
    num2: int = False
    client: Client = Client(
        'https://calculator-webservice.mybluemix.net/calculator?wsdl')

    @abstractmethod
    def calculate(self) -> int:
        raise NotImplementedError


class CalculatorSubtract(Calculator):
    def calculate(self):
        return self.client.service.subtract(self.num1, self.num2)


class CalculatorAdd(Calculator):
    def calculate(self):
        return self.client.service.add(self.num1, self.num2)


class CalculatorMultiply(Calculator):
    def calculate(self):
        return self.client.service.multiply(self.num1, self.num2)


class CalculatorDivide(Calculator):
    def calculate(self):
        return self.client.service.divide(self.num1, self.num2)
