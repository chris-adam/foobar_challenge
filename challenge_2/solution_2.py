import itertools
import random

def concat_list(l):
    """
    This function
    1. takes a list of integers;
    2. sort them by decreasing amount;
    3. concat the digits into a single integer.
    """
    if not l:
        return 0
    return int(''.join([str(digit) for digit in sorted(l, reverse=True)]))

def solution(l):
    l_copy = list(l)
    modulo_l = [elem % 3 for elem in l_copy]
    have_twin_1 = len([elem for elem in l_copy if elem % 3 == 1]) >= 2
    have_twin_2 = len([elem for elem in l_copy if elem % 3 == 2]) >= 2
    modulo_offset = sum(l_copy) % 3

    if modulo_offset == 0:
        return concat_list(l_copy)
    elif modulo_offset in modulo_l:
        l_copy.remove(min(filter(lambda x: x%3 == modulo_offset, l_copy)))
        return concat_list(l_copy)
    elif have_twin_1 or have_twin_2:
        l_copy.remove(min(filter(lambda x: x%3 == (3-modulo_offset), l_copy)))
        l_copy.remove(min(filter(lambda x: x%3 == (3-modulo_offset), l_copy)))
        return concat_list(l_copy)
    
    return 0


print(solution([8, 6, 2]))
