def multiply(a: float, b: float) -> float:
    '''

    Args:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of a and b.
    '''
    a = float(a)
    b = float(b)
    return a * b

def divide(a: float, b: float) -> float:
    '''

    Args:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float: The result of a divided by b.

    Raises:
    ValueError: If b is zero.
    '''
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
