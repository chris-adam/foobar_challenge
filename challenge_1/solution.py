import math

def solution(area):
    assert 1 <= area <= 10**6

    largest_square = int(math.floor(math.sqrt(area)) ** 2)
    remaining_area = area - largest_square

    if remaining_area >= 1:
        return [largest_square] + solution(remaining_area)
    else:
        return [largest_square]

print(solution(12))
