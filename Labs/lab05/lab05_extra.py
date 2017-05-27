from lab05 import *

## Extra Questions ##

# Q6
def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"
    lst_copy = lst[:]
    #list(lst)
    for i in range(len(lst_copy)):
        if not pred(lst_copy[i]):
            lst.remove(lst_copy[i])


# Q7
def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    "*** YOUR CODE HERE ***"
    lst_copy = lst[:]
    i = len(lst_copy) - 2
    while i >= 0:
        lst.remove(lst_copy[i])
        lst.append(lst_copy[i])
        i-=1


# Q8
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split() # .split() returns a list of the words in the string. Try printing it!
    "*** YOUR CODE HERE ***"
    word_dictionary = {}
    for word in word_list:
        word_dictionary[word] = 0

    for word in word_list:
        word_dictionary[word]+=1

    return word_dictionary


# Q9
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    pred = 0
    succ = 1
    counter = 0
    def fibnums():
        nonlocal counter, pred, succ
        if counter == 0:
            counter+=1
            return pred
        elif counter == 1:
            counter+=1
            return succ
        else:
            pred, succ = succ, succ+pred
            return succ
    return fibnums
