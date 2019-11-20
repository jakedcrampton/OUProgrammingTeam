# Solution for - https://open.kattis.com/problems/somesum
__author__ = "Taras Basiuk"

N = int(input().strip()) % 4
print("Odd" if N == 2 else "Even" if N == 0 else "Either")
