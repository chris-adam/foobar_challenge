# Quite interesting, I learned new things :)

# --- Docs
# Beatty sequences: https://en.wikipedia.org/wiki/Beatty_sequence
# Sum of Beatty sequence: https://math.stackexchange.com/a/2053713
# High precision python computing: https://stackoverflow.com/a/11523128

from decimal import Decimal, localcontext

def sum_beauty_sequence(n):
    with localcontext() as context:
        context.prec = 102  # Get just enough precision for this proclem

        if n == 0:
            return 0
        else:
            n_prime = int((Decimal(2).sqrt() - 1)*n)
            return n*n_prime + n*(n+1)/2 - n_prime*(n_prime+1)/2 - sum_beauty_sequence(n_prime)


def solution(str_n):
    n = int(str_n)
    res = sum_beauty_sequence(n)

    return str( int(res) )


print(solution('5'))  # A: 19
print(solution('77'))  # A: 4208
print(solution(str(10**100)))