# Solution for - https://open.kattis.com/problems/checkmateinone
__author__ = "Taras Basiuk"

"""
Straightforward solution which checks weather moving the rook
to threaten the enemy king results in the mate or not.
"""

# Enemy king, our king, and our rook coordinates: (row, column)
k = None
K = None
R = None

# Read in the coordinates from the input
for i in range(8):
    row = input().strip()

    if not k and row.find('k') != -1:
        k = (i, row.find('k'))

    if not K and row.find('K') != -1:
        K = (i, row.find('K'))

    if not R and row.find('R') != -1:
        R = (i, row.find('R'))

# Which cells out king threatens?
our_king_threats = set()
for m in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
    if K[0] + m[0] >= 0 and K[0] + m[0] <= 7 and K[1] + m[1] >= 0 and K[1] + m[1] <= 7:
        our_king_threats.add((K[0] + m[0], K[1] + m[1]))

checkmate = True

# Checkmate via row threat?

# Can our rook get to the same row as the enemy king (our king not in the way)?
if R[1] == K[1] and abs(R[0] - k[0]) >= abs(R[0] - K[0]):
    checkmate = False

# Can our rook threaten the enemy king (our king not in the way)?
if checkmate and k[0] == K[0] and abs(R[1] - k[1]) > abs(R[1] - K[1]):
    checkmate = False

# Can the enemy king just capture our rook?
if checkmate and ((k[1] - 1 == R[1] and ((k[0], k[1] - 1) not in our_king_threats)) or (k[1] + 1 == R[1] and ((k[0], k[1] + 1) not in our_king_threats))):
    checkmate = False

# Where can the enemy key run away from the row threat without being threatened by our king?
enemy_king_moves = set()
for m in [(1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
    if k[0] + m[0] >= 0 and k[0] + m[0] <= 7 and k[1] + m[1] >= 0 and k[1] + m[1] <= 7 and (k[0] + m[0], k[1] + m[1]) not in our_king_threats:
        enemy_king_moves.add((k[0] + m[0], k[1] + m[1]))

# Are the any saving moves for the enemy king?
if checkmate and enemy_king_moves:
    checkmate = False

# Checkmate via column threat?
if not checkmate:
    checkmate = True

    # Can our rook get to the same column as the enemy king (our king not in the way)?
    if R[0] == K[0] and abs(R[1] - k[1]) >= abs(R[1] - K[1]):
        checkmate = False

    # Can our rook threaten the enemy king (our king not in the way)?
    if checkmate and k[1] == K[1] and abs(R[0] - k[0]) > abs(R[0] - K[0]):
        checkmate = False

    # Can the enemy king just capture our rook?
    if checkmate and ((k[0] - 1 == R[0] and ((k[0] - 1, k[1]) not in our_king_threats)) or (k[0] + 1 == R[0] and ((k[0] + 1, k[1]) not in our_king_threats))):
        checkmate = False

    # Where can the enemy key run away from the column threat without being threatened by our king?
    enemy_king_moves = set()
    for m in [(0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if k[0] + m[0] >= 0 and k[0] + m[0] <= 7 and k[1] + m[1] >= 0 and k[1] + m[1] <= 7 and (k[0] + m[0], k[1] + m[1]) not in our_king_threats:
            enemy_king_moves.add((k[0] + m[0], k[1] + m[1]))

    # Are the any saving moves?
    if checkmate and enemy_king_moves:
        checkmate = False

# Print the output
print("Yes" if checkmate else "No")
