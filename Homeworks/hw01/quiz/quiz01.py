def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"

    smaller = min(a,b)
    bigger = max(a,b)
    if bigger%smaller==0:
        return smaller
    else:
        i=2
        while i<=smaller:
            n = bigger*i
            i+=1
            if n%smaller == 0:
                return n



def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"

    #the main code part
    i = 0
    total  = 0
    while i<10:
        a = has_digit(n,i)
        #print ( str(i) + "     " + str(a))
        total += a
        i=i+1
    return total


#the subcode
def has_digit(n,k):
    if n == k:
        return 1
    while n>0:
        rem = n%10
        n = n//10
        if rem == k:
            return 1
    return 0
