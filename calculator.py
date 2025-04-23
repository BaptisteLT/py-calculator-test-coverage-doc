import pytest

class Calculator:

    '''
        Multiplies two numbers and returns the result.

        Parameters:
        val1 (float | int): The first number.
        val2 (float | int): The second number.

        Returns:
        float: The product of val1 and val2.
    '''
    def multiply(self, val1:  float | int, val2:  float | int) -> float:
        return val1 * val2
    
    '''
        Adds two numbers and returns the result.

        Parameters:
        val1 (float | int): The first number.
        val2 (float | int): The second number.

        Returns:
        float: The sum of val1 and val2.
    '''
    def addition(self, val1: float | int, val2:  float | int) ->  float | int:
        return val1 + val2
    
    '''
        Subtracts two numbers and returns the result.

        Parameters:
        val1 (float | int): The first number.
        val2 (float | int): The second number.

        Returns:
        float: The result of val1 - val2.
    '''
    def substract(self, val1:  float | int, val2:  float | float | int) -> float:
        return val1 - val2
    
    '''
        Divides the first number by the second and returns the result.

        Parameters:
        val1 (float | int): The numerator.
        val2 (float | int): The denominator.

        Returns:
        float | None: The result of the division, or None if division by zero.
    '''
    def divide(self, val1:  float | int, val2:  float | int) ->  float | int | None:
        if (val2 == 0):
            return None
        return val1 / val2
