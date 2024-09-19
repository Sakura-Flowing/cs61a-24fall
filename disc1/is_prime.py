def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def find_factor(n):
    fact = n - 1
    while fact:
        if n % fact == 0:
            return fact
        fact -= 1
