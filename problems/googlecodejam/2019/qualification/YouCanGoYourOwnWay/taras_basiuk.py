# Solution for - https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
__author__ = "Taras Basiuk"

T = int(input().strip())
for i in range(1, T + 1):
    _ = input() # N is not needed
    P = list(input().strip())
    for j in range(len(P)):
        # Simply mirror Lydia's moves
        P[j] = 'E' if P[j] == 'S' else 'S'

    print("Case #{}: {}".format(i, ''.join(P)))
