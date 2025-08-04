import numpy as np
def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    ...

    Args:
    a: np.array
    b: np.array

    Returns:
    np.array
    '''

    # let's hope that both vectors have the same shape
    flat_a = a.reshape(-1)
    flat_b = b.reshape(-1)
    
    return np.multiply(flat_a, flat_b)

print(element_wise_multiply(np.array([[1, 2], [3, 4]]), np.array([[5, 6, 7, 8]])))