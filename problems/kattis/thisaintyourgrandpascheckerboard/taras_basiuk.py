# Solution for - https://open.kattis.com/problems/thisaintyourgrandpascheckerboard
__author__ = "Taras Basiuk"

N = int(input().strip())

correct = True

# Initialize column counts (W_num, B_num) and sequence tracker
collumn_counts = [(0, 0)] * N
collumn_sequence = [('placeholder', 0)] * N

# Iterate through rows
i = 0
while correct and i < N:
    row = input().strip()

    # Initialize row counts (W_num, B_num) and sequence tracker
    row_counts = (0, 0)
    row_sequence = ('placeholder', 0)

    # Iterate through the characters in the row
    j = 0
    while j < N:
        # Update the row and column counts with the current character
        if row[j] == 'W':
            row_counts = (row_counts[0] + 1, row_counts[1])
            collumn_counts[j] = (collumn_counts[j][0] + 1, collumn_counts[j][1])
        else:
            row_counts = (row_counts[0], row_counts[1] + 1)
            collumn_counts[j] = (collumn_counts[j][0], collumn_counts[j][1] + 1)

        # Update the row and column sequence trackers with the current character
        if row_sequence[0] == row[j]:
            row_sequence = (row_sequence[0], row_sequence[1] + 1)
        else:
            row_sequence = (row[j], 1)

        if collumn_sequence[j][0] == row[j]:
            collumn_sequence[j] = (collumn_sequence[j][0], collumn_sequence[j][1] + 1)
        else:
            collumn_sequence[j] = (row[j], 1)

        # Check that current row and column sequence in not too long
        if row_sequence[1] == 3 or collumn_sequence[j][1] == 3:
            correct = False
            break

        # If this is the last row, check that the column count is even
        if i == N - 1 and collumn_counts[j][0] != collumn_counts[j][1]:
            correct = False
            break

        j += 1

    # Check that the row count is even
    if correct and row_counts[0] != row_counts[1]:
        correct = False
        break

    i += 1

print(1 if correct else 0)
