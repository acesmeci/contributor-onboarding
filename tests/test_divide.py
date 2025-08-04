import numpy as np
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

def test_divide():
    # Test normal division
    assert divide(6, 2) == 3.0, "Expected 6 / 2 to be 3.0"
    assert divide(-9, 3) == -3.0, "Expected -9 / 3 to be -3.0"
    assert divide(0, 5) == 0.0, "Expected 0 / 5 to be 0.0"
    
    # Test division by zero
    try:
        divide(2, 0)
        print("Failed: No exception for divide by zero")
    except ValueError:
        print("Passed: Correctly raised ValueError for divide by zero")

    print("All other tests passed!")

if __name__ == "__main__":
    test_divide()