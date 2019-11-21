# Solution for - https://open.kattis.com/problems/pullingtheirweight
__author__ = "Taras Basiuk"

m = int(input().strip())

# Read in the animal wights and sort them
animals = []
for _ in range(m):
    animals.append(int(input().strip()))
animals = sorted(animals)

# Figure out the half weight of the animals (potentially including the one which will be discarded)
half_weight = sum(animals) / 2
curr_weight = 0

# Iterate through sorted animal weights adding them to one side of the sled
ti = 0
while ti < len(animals):
    curr_weight += animals[ti]

    # Current weight can only exceed the half weight when we add the weight of the to be discarded animal.
    # So the current animal is the target.
    if curr_weight > half_weight:
        print(animals[ti])
        break

    # Current weight can equal the half weight in two cases:
    # 1. We're in the middle of the animal group to be split. In this case current animal is the target.
    # 2. We're finished adding the group of animals of the same weight. So the target is current weight + 1.
    if curr_weight == half_weight:
        print(animals[ti] if animals[ti] == animals[ti + 1] else animals[ti] + 1)
        break

    ti += 1
