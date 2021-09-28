from abc import ABC, abstractmethod
from unittest import TestCase

from zeep.exceptions import Fault

from calculator import CalculatorSubtract, CalculatorAdd, CalculatorMultiply, CalculatorDivide, Calculator


class CalcBase(ABC):
    calc: Calculator

    @abstractmethod
    def test_booth_null(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_same_not_null_positive(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_same_not_null_negative(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_null_last_positive(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_null_last_negative(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_last_null_first_positive(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_last_null_first_negative(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_negative_last_positive_less(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_negative_last_positive_greater(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_both_negative_last_less(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_both_negative_last_greater(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_positive_last_negative_less(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_first_positive_last_negative_greater(self):
        raise NotImplementedError  # NOSONAR

    @abstractmethod
    def test_both_positive(self):
        raise NotImplementedError  # NOSONAR

    def test_has_calc(self):
        assert isinstance(self.calc.calculate(), int)


class TestSubtract(CalcBase, TestCase):
    calc = CalculatorSubtract()

    def test_booth_null(self):
        self.calc.num1 = self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 0)

    def test_same_not_null_positive(self):
        self.calc.num1 = self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 0)

    def test_same_not_null_negative(self):
        self.calc.num1 = self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 0)

    def test_first_null_last_positive(self):
        self.calc.num1 = 0
        self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), -4)

    def test_first_null_last_negative(self):
        self.calc.num1 = 0
        self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 4)

    def test_last_null_first_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 4)

    def test_last_null_first_negative(self):
        self.calc.num1 = -4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), -4)

    def test_first_negative_last_positive_less(self):
        self.calc.num1 = -4
        self.calc.num2 = 3
        self.assertEqual(self.calc.calculate(), -7)

    def test_first_negative_last_positive_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), -9)

    def test_both_negative_last_less(self):
        self.calc.num1 = -4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), -1)

    def test_both_negative_last_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), 1)

    def test_first_positive_last_negative_less(self):
        self.calc.num1 = 4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), 7)

    def test_first_positive_last_negative_greater(self):
        self.calc.num1 = 4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), 9)

    def test_both_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), -1)


class TestAdd(CalcBase, TestCase):
    calc = CalculatorAdd()

    def test_booth_null(self):
        self.calc.num1 = self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 0)

    def test_same_not_null_positive(self):
        self.calc.num1 = self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 8)

    def test_same_not_null_negative(self):
        self.calc.num1 = self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), -8)

    def test_first_null_last_positive(self):
        self.calc.num1 = 0
        self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 4)

    def test_first_null_last_negative(self):
        self.calc.num1 = 0
        self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), -4)

    def test_last_null_first_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 4)

    def test_last_null_first_negative(self):
        self.calc.num1 = -4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), -4)

    def test_first_negative_last_positive_less(self):
        self.calc.num1 = -4
        self.calc.num2 = 3
        self.assertEqual(self.calc.calculate(), -1)

    def test_first_negative_last_positive_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), 1)

    def test_both_negative_last_less(self):
        self.calc.num1 = -4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), -7)

    def test_both_negative_last_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), -9)

    def test_first_positive_last_negative_less(self):
        self.calc.num1 = 4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), 1)

    def test_first_positive_last_negative_greater(self):
        self.calc.num1 = 4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), -1)

    def test_both_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), 9)


class TestMultiply(CalcBase, TestCase):
    calc = CalculatorMultiply()

    def test_booth_null(self):
        self.calc.num1 = self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 0)

    def test_same_not_null_positive(self):
        self.calc.num1 = self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 16)

    def test_same_not_null_negative(self):
        self.calc.num1 = self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 16)

    def test_first_null_last_positive(self):
        self.calc.num1 = 0
        self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 0)

    def test_first_null_last_negative(self):
        self.calc.num1 = 0
        self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 0)

    def test_last_null_first_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 0)

    def test_last_null_first_negative(self):
        self.calc.num1 = -4
        self.calc.num2 = 0
        self.assertEqual(self.calc.calculate(), 0)

    def test_first_negative_last_positive_less(self):
        self.calc.num1 = -4
        self.calc.num2 = 3
        self.assertEqual(self.calc.calculate(), -12)

    def test_first_negative_last_positive_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), -20)

    def test_both_negative_last_less(self):
        self.calc.num1 = -4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), 12)

    def test_both_negative_last_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), 20)

    def test_first_positive_last_negative_less(self):
        self.calc.num1 = 4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), -12)

    def test_first_positive_last_negative_greater(self):
        self.calc.num1 = 4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), -20)

    def test_both_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), 20)


class TestDivide(CalcBase, TestCase):
    calc = CalculatorDivide()

    def test_booth_null(self):
        self.calc.num1 = self.calc.num2 = 0
        self.assertRaises(Fault, self.calc.calculate)

    def test_same_not_null_positive(self):
        self.calc.num1 = self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 1)

    def test_same_not_null_negative(self):
        self.calc.num1 = self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 1)

    def test_first_null_last_positive(self):
        self.calc.num1 = 0
        self.calc.num2 = 4
        self.assertEqual(self.calc.calculate(), 0)

    def test_first_null_last_negative(self):
        self.calc.num1 = 0
        self.calc.num2 = -4
        self.assertEqual(self.calc.calculate(), 0)

    def test_last_null_first_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 0
        self.assertRaises(Fault, self.calc.calculate)

    def test_last_null_first_negative(self):
        self.calc.num1 = -4
        self.calc.num2 = 0
        self.assertRaises(Fault, self.calc.calculate)

    def test_first_negative_last_positive_less(self):
        self.calc.num1 = -4
        self.calc.num2 = 3
        self.assertEqual(self.calc.calculate(), -1)

    def test_first_negative_last_positive_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), 0)

    def test_both_negative_last_less(self):
        self.calc.num1 = -4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), 1)

    def test_both_negative_last_greater(self):
        self.calc.num1 = -4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), 0)

    def test_first_positive_last_negative_less(self):
        self.calc.num1 = 4
        self.calc.num2 = -3
        self.assertEqual(self.calc.calculate(), -1)

    def test_first_positive_last_negative_greater(self):
        self.calc.num1 = 4
        self.calc.num2 = -5
        self.assertEqual(self.calc.calculate(), 0)

    def test_both_positive(self):
        self.calc.num1 = 4
        self.calc.num2 = 5
        self.assertEqual(self.calc.calculate(), 0)
