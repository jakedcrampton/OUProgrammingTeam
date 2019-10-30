# Solution for - https://open.kattis.com/problems/grille
__author__ = "Taras Basiuk"

# Read in the size of the grille
n = int(input().strip())

# Read in row and column positions of the holes 
holes = []
for i in range(n):
    row = input().strip()

    start = 0
    column = row.find(".") # Find the first hole in the row
    while column != -1: # Until there are no more holes
        holes.append((i, column))
        start = column + 1
        column = row.find(".", start) # Find the next hole

# Read in the cyphertext and prepare the plaintext of the same size
cyphertext = input().strip()
plain_characters = len(cyphertext)
plaintext = [None] * plain_characters

from operator import itemgetter

# Rotate the holes by 90 degrees and sort them by row and column
rotated90_holes = []
for h in holes:
    rotated90_holes.append((h[1], (n - 1) - h[0]))

rotated90_holes = sorted(rotated90_holes, key=itemgetter(1))
rotated90_holes = sorted(rotated90_holes, key=itemgetter(0))

# Rotate the holes by 180 degrees and sort them by row and column
rotated180_holes = []
for h in rotated90_holes:
    rotated180_holes.append((h[1], (n - 1) - h[0]))

rotated180_holes = sorted(rotated180_holes, key=itemgetter(1))
rotated180_holes = sorted(rotated180_holes, key=itemgetter(0))

# Rotate the holes by 270 degrees and sort them by row and column
rotated270_holes = []
for h in rotated180_holes:
    rotated270_holes.append((h[1], (n - 1) - h[0]))

rotated270_holes = sorted(rotated270_holes, key=itemgetter(1))
rotated270_holes = sorted(rotated270_holes, key=itemgetter(0))

# Collect all holes
holes += rotated90_holes + rotated180_holes + rotated270_holes

 # If there are not enough holes for the cyphertext, grille is invalid
valid = len(cyphertext) == len(holes)

i = 0
while valid and i < len(cyphertext): # For each character in cyphertext
    # Find corresponding plaintext character
    plaintext_index = (holes[i][0] * n) + holes[i][1]

    if not plaintext[plaintext_index]:
        # Enter the plaintext character
        plaintext[plaintext_index] = cyphertext[i]
        plain_characters -= 1
    else:
        # If plaintext character is already found, grille is invalid
        valid = False

    i += 1

if valid and plain_characters == 0: # If all plaintext characters found
    print("".join(plaintext))
else:
    print("invalid grille")
