from utils import *

# Q1
from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """

    lat1 = get_lat(city1)
    lat2 = get_lat(city2)
    lon1 = get_lon(city1)
    lon2 = get_lon(city2)
    latsq = (lat1-lat2)**2
    lonsq = (lon1-lon2)**2

    return sqrt (latsq+lonsq)

# Q2
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """

    maincity = make_city('maincity', lat, lon)
    main_to_1 = distance(maincity,city1)
    main_to_2 = distance(maincity,city2)

    return get_name(city1) if main_to_1<main_to_2 else get_name(city2)
# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b==0 or a == 0:
        return c
    elif b==1:
        return  a + c
    else:
        return a + ab_plus_c(a,(b-1), c)


# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    if n ==2:
        return True
    else:
        return helperfunc(n,2)


def helperfunc(n,i):
    if n%i==0:
        return False
    elif i == n//2  and n%i !=0:
        return True
    else:
        return helperfunc(n,i+1)
