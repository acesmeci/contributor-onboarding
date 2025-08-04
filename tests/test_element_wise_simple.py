import numpy as np
from src.utils import element_wise_multiply 

def test_element_wise_multiply_basic():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6, 7, 8]])
    expected = np.array([5, 12, 21, 32])

    result = element_wise_multiply(a, b)

    assert np.array_equal(result, expected), f"Expected {expected}, got {result}
