# Solution - https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb
__author__ = "Taras Basiuk"

T = int(input().strip())
for i in range(1, T + 1):
    N = int(input().strip())
    L = list(map(int, input().strip().split()))

    # Unzip the list into its even and odd indexed elements and sort them
    # (that's a shorter version of what trouble sort does)
    evens = sorted(L[0::2])
    odds = sorted(L[1::2])

    # Compare corresponding even and odd element to check whether the sorting is valid
    for j in range(len(evens)):
        if j < len(odds) and odds[j] < evens[j]:
            print("Case #{}: {}".format(i, 2 * j))
            break
        if j + 1 < len(evens) and evens[j + 1] < odds[j]:
            print("Case #{}: {}".format(i, (2 * j) + 1))
            break
    else:
        print("Case #{}: OK".format(i))
