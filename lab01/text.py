def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
    if start == stop:
        return start
    return add_in_range(start + 1, stop) + start
    # ret = 0
    # for i in range(start, stop + 1):
    #     print(i)
    #     ret += i
    # return ret


x = add_in_range(3, 5)
print(x)