
def get_roots_quadratic(a, b, c):
    """
    Returns the roots of a quadratic equation using the coefficients.
    """
    root1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
    root2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / 2 * a
    
    return root1, root2
