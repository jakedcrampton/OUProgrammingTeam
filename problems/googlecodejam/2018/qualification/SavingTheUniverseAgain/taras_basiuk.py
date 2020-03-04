# Solution - https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966
__author__ = "Taras Basiuk"

# Calculates the robot's damage
def get_damage(P):
    power = 1
    damage = 0
    for c in P:
        if c == 'C':
            power *= 2 # Robot powers up
        else:
            damage += power # Robot shoots

    return damage

T = int(input().strip())
for i in range(1, T + 1):
    D, P = input().strip().split()
    D, P = int(D), list(P)

    # Get initial damage and check whether any checks are needed
    damage = get_damage(P)
    if damage <= D:
        print("Case #{}: 0".format(i))
        continue

    # Iterate through the string backwards swapping 'C' and 'S' as soon as possible
    swap_i = len(P) - 2
    swaps = 0
    while swap_i >= 0:
        if P[swap_i] == 'C' and P[swap_i + 1] == 'S':
            P[swap_i] = 'S'
            P[swap_i + 1] = 'C'
            if swap_i < len(P) - 2: # Have to backtrack after the swap
                swap_i += 1
            swaps += 1

            # Check whether we made enough swaps
            damage = get_damage(P)
            if damage <= D:
                print("Case #{}: {}".format(i, swaps))
                break
        else:
            swap_i -= 1
    else:
        # We made all the possible swaps and did not break out of the loop
        print("Case #{}: IMPOSSIBLE".format(i))
