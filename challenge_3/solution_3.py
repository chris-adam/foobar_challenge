def solution(l):
    lucky_triple_count = 0
    
    lucky_double_list = list()
    for elem_i, elem in enumerate(l):
        lucky_double_list.append([el for el in l[elem_i+1:] if el%elem == 0])

    l_copy = list(l)
    for lucky_double_i, lucky_double in enumerate(lucky_double_list):
        l_copy[lucky_double_i] = 0
        l_tmp = list(l_copy)
        for elem in lucky_double:
            lucky_double_index = l_tmp.index(elem)
            lucky_triple_count += len(lucky_double_list[lucky_double_index])
            l_tmp[lucky_double_index] = 0

    # for lucky_double_i, lucky_double in enumerate(lucky_double_list):
    #     l_tmp = list(l)[lucky_double_i+1:]
    #     for elem_i, elem in enumerate(lucky_double):
    #         lucky_double_index = l_tmp[elem_i:].index(elem) + lucky_double_i+elem_i+1
    #         lucky_triple_count += len(lucky_double_list[lucky_double_index])
    
    return lucky_triple_count


print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([2, 4, 8, 16]))
