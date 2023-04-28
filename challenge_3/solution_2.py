import random

def solution(x, y):
    # print(x, y)
    x_int, y_int = int(x), int(y)
    x_int, y_int = max(x_int, y_int), min(x_int, y_int)

    if y_int == 1:
        return str(x_int-1)

    i = 0
    result = (x_int, y_int)
    x_result, y_result = result
    while x_result > 1 and (x_result % y_result != 0 or y_result == 1):
        n_steps = x_result // y_result
        result = max(x_result-y_result*n_steps, y_result), min(x_result-y_result*n_steps, y_result)
        i += n_steps
        x_result, y_result = result
        # print((x_int, y_int), x_result, y_result, n_steps)
        # print(result, n_steps)

    if x_result == 1:
        if y_result == 0:
            i -= 1
        return str(int(i))

    return "impossible"


print(solution("2", "1"))
print(solution("4", "7"))
print(solution("2", "4"))

print(solution("14", "7"))

# for _ in range(100):
#     num_1 = random.randint(1, 20)
#     num_2 = random.randint(1, 20)
#     print(solution(str(num_1), str(num_2)))
#     print
