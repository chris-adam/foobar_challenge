import random
from operator import xor

# Ref: https://www.geeksforgeeks.org/find-xor-of-numbers-from-the-range-l-r/
# Function to return the XOR of elements
# from the range [l, r]
def findXORFun(l, r):
    def findXOR(n):
        mod = n % 4;
    
        # If n is a multiple of 4
        if (mod == 0):
            return n
    
        # If n % 4 gives remainder 1
        elif (mod == 1):
            return 1
    
        # If n % 4 gives remainder 2
        elif (mod == 2):
            return n + 1
    
        # If n % 4 gives remainder 3
        elif (mod == 3):
            return 0
    return (xor(findXOR(l - 1) , findXOR(r)))


def solution(start, length):
    checksum = 0
    for size in range(length, 0, -1):
        checksum ^= findXORFun(start, start + size - 1)
        start += length

    return checksum


# for _ in range(1000000):
#     start = random.randint(0, 200000000)
#     length = random.randint(1, 200000000)
#     print(solution(start, length))

print(solution(0, 3))
print(solution(17, 4))
