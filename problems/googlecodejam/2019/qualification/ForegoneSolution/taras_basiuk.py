# Solution for - https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
__author__ = "Taras Basiuk"

T = int(input().strip())
for i in range(1, T + 1):
    """
        For every test case, 'split' the N into A and B, where A is N with every '4' replaced by '2'
        and B is the difference between N and A.
    """
    N = int(input().strip())
    N_copy = N

    A = 0
    m = 1 # Digit indicator
    while N > 0:
        d = N % 10 # Last digit
        A = (d * m) + A if d != 4 else (2 * m) + A # If last digit is not 4 add it to A, otherwise add 2
        N = N // 10 # Switch to the next digit
        m *= 10 # Increase digit indicator
        
    print("Case #{}: {} {}".format(i, A, N_copy - A))
