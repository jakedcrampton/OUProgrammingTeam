# Solution for - https://open.kattis.com/problems/zipfsong
__author__ = "Taras Basiuk"

# Read in the input
n, m = tuple(map(int, input().strip().split()))

# Populate the album
album = []
for i in range(1, n + 1):
    fi, name = input().strip().split()
    album.append((int(fi) * i, name)) # Perform zipfian adjustment

# Sort on the adjusted listens. Secondary sorting on order in the album was already implicitly done
from operator import itemgetter
album = sorted(album, key=itemgetter(0), reverse=True)

# Output the result
for i in range(m):
    print(album[i][1])
