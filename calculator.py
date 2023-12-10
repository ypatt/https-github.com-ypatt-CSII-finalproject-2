
import math

class Calculator:
    """
    Calculator class provides common mathematical operations.

    Methods:
    - add(a: float, b: float) -> float: Add two numbers.
    - subtract(a: float, b: float) -> float: Subtract one number from another.
    - multiply(a: float, b: float) -> float: Multiply two numbers.
    - divide(a: float, b: float) -> float: Divide one number by another.
    - power(a: float, b: float) -> float: Calculate the power of a number.
    - factorial(a: int) -> int: Calculate the factorial of a non-negative integer.
    - natural_log(a: float) -> float: Calculate the natural logarithm of a positive number.
    - square_root(a: float) -> float: Calculate the square root of a non-negative number.
    - exp(a: float) -> float: Calculate the exponential function of a number.
    - validate_input(*args): Validate that input values are numeric (int or float).
    - check_overflow(result): Check if the calculation result exceeds the maximum limit.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Add two numbers.

        Parameters:
        - a (float): The first operand.
        - b (float): The second operand.

        Returns:
        float: The result of the addition.
        """

        result = a + b
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Subtract one number from another.

        Parameters:
        - a (float): The minuend.
        - b (float): The subtrahend.

        Returns:
        float: The result of the subtraction.
        """

        result = a - b
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.

        Parameters:
        - a (float): The first factor.
        - b (float): The second factor.

        Returns:
        float: The result of the multiplication.
        """
        result = a * b
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divide one number by another.

        Parameters:
        - a (float): The numerator.
        - b (float): The denominator.

        Returns:
        float: The result of the division.

        Raises:
        ValueError: If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Error: Cannot divide by zero. Please enter a valid denominator.")
        result = a / b
        return result

    @staticmethod
    def power(a: float, b: float) -> float:
        """
        Calculate the power of a number.

        Parameters:
        - a (float): The base.
        - b (float): The exponent.

        Returns:
        float: The result of the exponentiation.
        """
        return math.pow(a, b)

    @staticmethod
    def factorial(a: int) -> int:
        """
        Calculate the factorial of a non-negative integer.

        Parameters:
        - a (int): The non-negative integer.

        Returns:
        int: The result of the factorial.

        Raises:
        ValueError: If the input is negative.
        """
        if a < 0:
            raise ValueError("Error: Cannot compute the factorial of a negative number.")
        return math.factorial(a)

    @staticmethod
    def natural_log(a: float) -> float:
        """
        Calculate the natural logarithm of a positive number.

        Parameters:
        - a (float): The positive number.

        Returns:
        float: The natural logarithm of the input.

        Raises:
        ValueError: If the input is non-positive.
        """
        if a <= 0:
            raise ValueError("Error: Cannot calculate the natural logarithm of a negative number.")
        return math.log(a)

    @staticmethod
    def square_root(a: float) -> float:
        """
        Calculate the natural logarithm of a positive number.

        Parameters:
        - a (float): The positive number.

        Returns:
        float: The natural logarithm of the input.

        Raises:
        ValueError: If the input is non-positive.
        """
        if a < 0:
            raise ValueError("Error: Cannot calculate the square root of a negative number.")
        return math.sqrt(a)

    @staticmethod
    def exp(a: float) -> float:
        """
        Calculate the exponential function of a number.

        Parameters:
        - a (float): The exponent.

        Returns:
        float: The result of the exponential function.
        """
        result = math.exp(a)
        return result

    @staticmethod
    def validate_input(*args):
        """
        Validate that input values are numeric (int or float).

        Parameters:
        *args: Variable number of arguments to validate.

        Raises:
        ValueError: If any argument is not a numeric value.
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Error: Invalid input. Please enter a numeric value.")

    @staticmethod
    def check_overflow(result):
        """
        Check if the calculation result exceeds the maximum limit.

        Parameters:
        - result (float): The result of a calculation.

        Raises:
        OverflowError: If the result exceeds the maximum limit of 10 seconds.
        """
        if result > 1e100:
            raise OverflowError("Error: Calculation result exceeds the maximum limit.")
