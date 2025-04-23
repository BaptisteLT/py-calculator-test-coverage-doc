import pytest
from calculator import Calculator 

class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_multiply_valid(self):
        assert self.calculator.multiply(3, 3) == 9
        assert self.calculator.multiply(-100, 10) == -1000
        assert self.calculator.multiply(2.5, 4.0) == 10.0
        assert self.calculator.multiply(1e10, 2) == 2e10

    def test_addition_valid(self):
        assert self.calculator.addition(3, 3) == 6
        assert self.calculator.addition(-3, 2) == -1
        assert self.calculator.addition(0.5, 0.5) == 1

    def test_substract_valid(self):
        assert self.calculator.substract(3, 3) == 0
        assert self.calculator.substract(-3, -4) == 1
        assert self.calculator.substract(-50, 4) == -54
        assert self.calculator.substract(0.5, 0.5) == 0

    def test_divide_valid(self):
        assert self.calculator.divide(3, 3) == 1
        assert self.calculator.divide(30, -3) == -10
        assert self.calculator.divide(5.5, 2.0) == 2.75
        assert self.calculator.divide(1e-10, 1) == 1e-10

    def test_divide_invalid(self):
        assert self.calculator.divide(10, 0) is None
