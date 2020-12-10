import numpy as np


def dot(a, b):
    """Compute the dot product of a and b.

    Arguments:
        a: Array of shape (2,).
        b: Array of shape (2,).

    Returns:
        dot_product: Dot product of a and b.
    """

    # Reshape a and b:
    a_rsh = a.reshape((2, 1))
    b_rsh = b.reshape((2, 1))

    # Compute the dot product of a and b:
    dot_product = np.matmul(np.transpose(a_rsh), b_rsh)
    dot_product = float(dot_product)

    return dot_product


# Test your code before you submit:
a = np.array([1, 0])
b = np.array([0, 1])
print(f'Vector a: {a}')
print(f'Vector b: {b}')
print(f'Dot product of a and b: {dot(a, b)}')
