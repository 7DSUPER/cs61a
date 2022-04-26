import re


def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
    # if start == stop:
    #     return start
    # return add_in_range(start + 1, stop) + start
    ret = 0
    for i in range(start, stop + 1):
        ret += i
    return ret

def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    for i in range(k, len(n)):
        if k == int(n[i]):
            return True 
    return False

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    ret = 1
    if k == 0:
        return ret
    for i in range(0, k):
        ret *= n
        n -= 1
    return ret

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # y = str(y)
    ret = 0
    # for i in range(len(y)):
    #     ret += int(y[i])
    # return ret
    while y:
        ret += y % 10
        y //= 10
    return ret


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = 0
    while n:
        if(n % 10 == 8):
            flag += 1
        elif(flag == 1 and n % 10 != 8):
            flag -= 1
        if(flag == 2):
            return True
        n //= 10
    return False

def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
    res = 0
    if num == 0:
        return res
    while num:
        if k == num % 10:
            res += 1
        num //= 10
    return res

# from doctest import run_docstring_examples
# run_docstring_examples(add_in_range, globals(), True)
# run_docstring_examples(digit_pos_match, globals(), True)
# run_docstring_examples(k_occurrence, globals(), True)