def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    mult = b
    while mult:
        if (mult % a == 0) & (mult % b == 0):
            return mult
        mult += 1
