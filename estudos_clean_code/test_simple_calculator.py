from unittest import TestCase

from simple_calculator import SimpleCalculator


class OperatorTestBase(TestCase):
    class Meta:
        abstract = True

    def setUp(self) -> None:
        self.calc = SimpleCalculator()


class TestAdd(OperatorTestBase):

    def test_booth_null(self):
        number_1 = number_2 = 0
        self.assertEqual(self.calc.add(number_1, number_2), 0)

    def test_same_not_null_positive(self):
        number_1 = number_2 = 4
        self.assertEqual(self.calc.add(number_1, number_2), 8)

    def test_same_not_null_negative(self):
        number_1 = number_2 = -4
        self.assertEqual(self.calc.add(number_1, number_2), -8)

    def test_first_null_last_positive(self):
        number_1 = 0
        number_2 = 4
        self.assertEqual(self.calc.add(number_1, number_2), 4)

    def test_first_null_last_negative(self):
        number_1 = 0
        number_2 = -4
        self.assertEqual(self.calc.add(number_1, number_2), -4)

    def test_last_null_first_positive(self):
        number_1 = 4
        number_2 = 0
        self.assertEqual(self.calc.add(number_1, number_2), 4)

    def test_last_null_first_negative(self):
        number_1 = -4
        number_2 = 0
        self.assertEqual(self.calc.add(number_1, number_2), -4)

    def test_first_negative_last_positive_less(self):
        number_1 = -4
        number_2 = 3
        self.assertEqual(self.calc.add(number_1, number_2), -1)

    def test_first_negative_last_positive_greater(self):
        number_1 = -4
        number_2 = 5
        self.assertEqual(self.calc.add(number_1, number_2), 1)

    def test_both_negative_last_less(self):
        number_1 = -4
        number_2 = -3
        self.assertEqual(self.calc.add(number_1, number_2), -7)

    def test_both_negative_last_greater(self):
        number_1 = -4
        number_2 = -5
        self.assertEqual(self.calc.add(number_1, number_2), -9)

    def test_first_positive_last_negative_less(self):
        number_1 = 4
        number_2 = -3
        self.assertEqual(self.calc.add(number_1, number_2), 1)

    def test_first_positive_last_negative_greater(self):
        number_1 = 4
        number_2 = -5
        self.assertEqual(self.calc.add(number_1, number_2), -1)

    def test_both_positive(self):
        number_1 = 4
        number_2 = 5
        self.assertEqual(self.calc.add(number_1, number_2), 9)


class TestSubtract(OperatorTestBase):

    def test_booth_null(self):
        number_1 = number_2 = 0
        self.assertEqual(self.calc.subtract(number_1, number_2), 0)

    def test_same_not_null_positive(self):
        number_1 = number_2 = 4
        self.assertEqual(self.calc.subtract(number_1, number_2), 0)

    def test_same_not_null_negative(self):
        number_1 = number_2 = -4
        self.assertEqual(self.calc.subtract(number_1, number_2), 0)

    def test_first_null_last_positive(self):
        number_1 = 0
        number_2 = 4
        self.assertEqual(self.calc.subtract(number_1, number_2), -4)

    def test_first_null_last_negative(self):
        number_1 = 0
        number_2 = -4
        self.assertEqual(self.calc.subtract(number_1, number_2), 4)

    def test_last_null_first_positive(self):
        number_1 = 4
        number_2 = 0
        self.assertEqual(self.calc.subtract(number_1, number_2), 4)

    def test_last_null_first_negative(self):
        number_1 = -4
        number_2 = 0
        self.assertEqual(self.calc.subtract(number_1, number_2), -4)

    def test_first_negative_last_positive_less(self):
        number_1 = -4
        number_2 = 3
        self.assertEqual(self.calc.subtract(number_1, number_2), -7)

    def test_first_negative_last_positive_greater(self):
        number_1 = -4
        number_2 = 5
        self.assertEqual(self.calc.subtract(number_1, number_2), -9)

    def test_both_negative_last_less(self):
        number_1 = -4
        number_2 = -3
        self.assertEqual(self.calc.subtract(number_1, number_2), -1)

    def test_both_negative_last_greater(self):
        number_1 = -4
        number_2 = -5
        self.assertEqual(self.calc.subtract(number_1, number_2), 1)

    def test_first_positive_last_negative_less(self):
        number_1 = 4
        number_2 = -3
        self.assertEqual(self.calc.subtract(number_1, number_2), 7)

    def test_first_positive_last_negative_greater(self):
        number_1 = 4
        number_2 = -5
        self.assertEqual(self.calc.subtract(number_1, number_2), 9)

    def test_both_positive(self):
        number_1 = 4
        number_2 = 5
        self.assertEqual(self.calc.subtract(number_1, number_2), -1)


class TestMultiply(OperatorTestBase):

    def test_booth_null(self):
        number_1 = number_2 = 0
        self.assertEqual(self.calc.multiply(number_1, number_2), 0)

    def test_same_not_null_positive(self):
        number_1 = number_2 = 4
        self.assertEqual(self.calc.multiply(number_1, number_2), 16)

    def test_same_not_null_negative(self):
        number_1 = number_2 = -4
        self.assertEqual(self.calc.multiply(number_1, number_2), 16)

    def test_first_null_last_positive(self):
        number_1 = 0
        number_2 = 4
        self.assertEqual(self.calc.multiply(number_1, number_2), 0)

    def test_first_null_last_negative(self):
        number_1 = 0
        number_2 = -4
        self.assertEqual(self.calc.multiply(number_1, number_2), 0)

    def test_last_null_first_positive(self):
        number_1 = 4
        number_2 = 0
        self.assertEqual(self.calc.multiply(number_1, number_2), 0)

    def test_last_null_first_negative(self):
        number_1 = -4
        number_2 = 0
        self.assertEqual(self.calc.multiply(number_1, number_2), 0)

    def test_first_negative_last_positive_less(self):
        number_1 = -4
        number_2 = 3
        self.assertEqual(self.calc.multiply(number_1, number_2), -12)

    def test_first_negative_last_positive_greater(self):
        number_1 = -4
        number_2 = 5
        self.assertEqual(self.calc.multiply(number_1, number_2), -20)

    def test_both_negative_last_less(self):
        number_1 = -4
        number_2 = -3
        self.assertEqual(self.calc.multiply(number_1, number_2), 12)

    def test_both_negative_last_greater(self):
        number_1 = -4
        number_2 = -5
        self.assertEqual(self.calc.multiply(number_1, number_2), 20)

    def test_first_positive_last_negative_less(self):
        number_1 = 4
        number_2 = -3
        self.assertEqual(self.calc.multiply(number_1, number_2), -12)

    def test_first_positive_last_negative_greater(self):
        number_1 = 4
        number_2 = -5
        self.assertEqual(self.calc.multiply(number_1, number_2), -20)

    def test_both_positive(self):
        number_1 = 4
        number_2 = 5
        self.assertEqual(self.calc.multiply(number_1, number_2), 20)


class TestDivide(OperatorTestBase):

    def test_booth_null(self):
        number_1 = number_2 = 0
        self.assertRaises(ValueError, self.calc.divide, number_1, number_2)

    def test_same_not_null_positive(self):
        number_1 = number_2 = 4
        self.assertEqual(self.calc.divide(number_1, number_2), 1)

    def test_same_not_null_negative(self):
        number_1 = number_2 = -4
        self.assertEqual(self.calc.divide(number_1, number_2), 1)

    def test_first_null_last_positive(self):
        number_1 = 0
        number_2 = 4
        self.assertEqual(self.calc.divide(number_1, number_2), 0)

    def test_first_null_last_negative(self):
        number_1 = 0
        number_2 = -4
        self.assertEqual(self.calc.divide(number_1, number_2), 0)

    def test_last_null_first_positive(self):
        number_1 = 4
        number_2 = 0
        self.assertRaises(ValueError, self.calc.divide, number_1, number_2)

    def test_last_null_first_negative(self):
        number_1 = -4
        number_2 = 0
        self.assertRaises(ValueError, self.calc.divide, number_1, number_2)

    def test_first_negative_last_positive_less(self):
        number_1 = -4
        number_2 = 2
        self.assertEqual(self.calc.divide(number_1, number_2), -2)

    def test_first_negative_last_positive_greater(self):
        number_1 = -4
        number_2 = 5
        self.assertEqual(self.calc.divide(number_1, number_2), -0.8)

    def test_both_negative_last_less(self):
        number_1 = -4
        number_2 = -2
        self.assertEqual(self.calc.divide(number_1, number_2), 2)

    def test_both_negative_last_greater(self):
        number_1 = -4
        number_2 = -5
        self.assertEqual(self.calc.divide(number_1, number_2), 0.8)

    def test_first_positive_last_negative_less(self):
        number_1 = 4
        number_2 = -2
        self.assertEqual(self.calc.divide(number_1, number_2), -2)

    def test_first_positive_last_negative_greater(self):
        number_1 = 4
        number_2 = -5
        self.assertEqual(self.calc.divide(number_1, number_2), -0.8)

    def test_both_positive(self):
        number_1 = 4
        number_2 = 5
        self.assertEqual(self.calc.divide(number_1, number_2), 0.8)
