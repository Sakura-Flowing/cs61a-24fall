def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    factor = n // 2
    # 我们只需从n//2开始寻找n的最大因数即可
    # n%factor==0 -> n//factor==2,3,4,5,6......
    # 所以n的最大因子，一定是从n//2开始的，更小的因数可能是n//3，n//4等等，知道factor==1

    while factor >= 1:
        if n % factor == 0:
            return factor
        factor -= 1
    return 1
