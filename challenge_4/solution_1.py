def is_loop(p1, p2):
    def is_power_of_two(x):
        if x == 0:
            return False
        return x & (x-1) == 0
    
    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a >= b:
            return gcd(b, a % b)
        return gcd(a, b % a)
    
    if sum((p1, p2)) % 2 != 0:
        return True
    if p1 == p2:
        return False
    if is_power_of_two(sum((p1, p2)) // gcd(p1, p2)):
        return False
    return True

def solution(banana_list):
    banana_list = sorted(banana_list)
    pairs_indices = list()
    for i, player_1 in enumerate(banana_list):
        pairs_indices.append({j+i+1 for j, player_2 in enumerate(banana_list[i+1:]) if is_loop(player_1, player_2)})

    pairs_count = 0
    picked_indices = set()
    for i, row in enumerate(pairs_indices):
        # If trainer is already fighting with someone earlier in the list
        if i in picked_indices:
            continue

        # Remove trainers picked by previous trainers
        row -= picked_indices

        # If there is no one to fight, pass
        if not row:
            continue

        # Let's assign a pair
        picked_index = row.pop()
        picked_indices.add(picked_index)
        pairs_count += 2

    return len(banana_list) - pairs_count

print(solution([1, 7, 3, 21, 13, 19]))
print(solution(list(range(1, 40))))
