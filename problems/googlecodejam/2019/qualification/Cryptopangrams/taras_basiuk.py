# Solution for - https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
__author__ = "Taras Basiuk"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

T = int(input().strip())

for i in range(1, T + 1):
    N, L = tuple(map(int, input().strip().split()))
    C = list(map(int, input().strip().split())) # Cypher text
    P = [None] * (len(C) + 1) # Plain text

    """
        When two adjacent cyphertext numbers are not equal,
        we can extract the corresponding plain text prime
        shared by them, by calculating their GCD
    """
    for j in range(len(C) - 1):
        if C[j] != C[j + 1]:
            P[j + 1] = gcd(C[j], C[j + 1])

    """
        If we found one plain text prime, but not the next one,
        we can found the next one by doing P[j + 1] = C[j] // P[j]
    """
    for j in range(len(P) - 1):
        if P[j + 1] == None and P[j] != None:
            P[j + 1] = C[j] // P[j]

    """
        Now we doing a very similar thing to above, but going
        backwards. Doing these two passes should eliminate
        every empty space in the plain text primes array
    """
    for j in range(len(P) - 1, 0, -1):
        if not P[j - 1] and P[j]:
            P[j - 1] = C[j - 1] // P[j]

    # Extract all unique primes and sort them
    letters = list(sorted(list(set(P))))

    # Build a mapping from the sorted unique primes to the letters
    key = {}
    for j in range(26):
        key[letters[j]] = alphabet[j]

    # Replace the primes with letters
    for j in range(len(P)):
        P[j] = key[P[j]]

    print("Case #{}: {}".format(i, "".join(P)))
