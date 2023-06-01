# def test_func():
#     #computes 2+2
#     assert 2+2 == 4

def test_calculate_fibonacci():
    """Calculates the nth Fibonacci value.

    Args:
        n (int): The index of the desired Fibonacci value.

    Returns:
        The nth Fibonacci value.
    """
    # Base cases
    n= 5
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return test_calculate_fibonacci(n-1) + test_calculate_fibonacci(n-2)
