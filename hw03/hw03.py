
HW_SOURCE_FILE = __file__

def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        return num == prev_digit
    last = num % 10
    cur = num // 10
    return (last == prev_digit or cur % 10 == last) + neighbor_digits(cur, last)
    

def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    if n > 0 and seq <= 0:
        return True
    if n < 10:
        if seq > 10 or seq != n:
            return False
    n_last = n % 10
    n_cur = n // 10
    seq_last = seq % 10
    seq_cur = seq // 10
    if n_last == seq_last:
        return has_subseq(n_cur, seq_cur)
    else:
        return has_subseq(n_cur, seq)


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos <= 0:
        return 0
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return num_eights(pos // 10)

def find_8(num):
    if num_eights(num) or (num % 8 == 0):
        return True
    else:
        return False

def count_8(num):
    i = 1
    count = 0
    while i <= num:
        if find_8(i):
            count += 1
        i += 1
    return count % 2

def for_1(bo):
    return -1 if bo else 1

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    # i, j = 0, 1
    # flag = True
    # while j <= n:
    #     if flag:
    #         i = add_n(i)
    #     else:
    #         i = sub_n(i)
    #     flag = find_8(j, flag)
    #     j += 1
    # return i
    def func1(i, ret, step):
        if i == n:
            return ret
        return func1(i + 1, ret + for_1(count_8(i)), for_1(count_8(i)))
    return func1(1, 1, 1)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def get_num_to_small(num):
    if num >= 25:
        return 25
    elif num < 25 and num >= 10:
        return 10
    elif num < 10 and num >= 5:
        return 5

def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def func1(change, smaller_change):
        if change < 0:
            return 0
        if change == 0:
            return 1
        if smaller_change == None:
            return 0
        return func1(change - smaller_change, \
             smaller_change) \
                 + func1(change, get_smaller_coin(smaller_change))
    return func1(change, 25)