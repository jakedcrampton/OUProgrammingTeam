# For - https://open.kattis.com/problems/gears2
# Generates a 32x32 square of equal sized gears
__author__ = "Taras Basiuk"

print(1024)
for i in range(32):
    for j in range(32):
        print("{} {} 1".format(i * 2, j * 2))
