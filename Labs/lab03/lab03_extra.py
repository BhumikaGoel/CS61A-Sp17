from lab03 import *

# Q6
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """

    if n == 0:
        return even_term(n)
    elif n == 1:
        return odd_term(n)
    else:
        if is_even(n):
            return even_term(n) + interleaved_sum(n-1, odd_term, even_term)
        else:
            return odd_term(n) + interleaved_sum(n-1, odd_term, even_term)


def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

# Q9
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: (y*10) + (x%10)
    while x > 0:
        x, y = x//10, f()
    return y == n

# Q10

def count_digit(n, x):
    if n == 0:
        return 0
    else:
        if n%10 == x:
            return 1 + count_digit(n//10, x)
        else:
            return count_digit(n//10, x)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    
    if n <10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)
