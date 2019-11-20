# Solution for - https://open.kattis.com/problems/flippingpatties
__author__ = "Taras Basiuk"

N = int(input().strip())

# Record how many actions the cooks will have to take at any given second
timeline_actions = {}
for _ in range(N):
    d, t = tuple(map(int, input().strip().split()))

    # Record one action per placing, flipping and giving patty to the customer
    for i in [t, t - d, t - (2 * d)]:
        timeline_actions[i] = 1 if i not in timeline_actions else timeline_actions[i] + 1

# Find the most number of actions cooks will have to perform in a second
max_actions = 0
for key in timeline_actions:
    max_actions =  timeline_actions[key] if timeline_actions[key] > max_actions else max_actions

# Calculate the number of required cooks
print((max_actions // 2) + (max_actions % 2))
