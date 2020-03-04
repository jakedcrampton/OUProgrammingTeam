#Solution for - https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007a30
__author__ = "Taras Basiuk"

T = int(input().strip())
for i in range(1, T + 1):
    A = int(input().strip())

    # Total number of 3 cell columns the gopher needs to prepare
    tot_col_x = (A // 3) + 1 if A % 3 != 0 else 0
    mid_col_x = 2 # Current X coordinate of a middle column where the gopher is deployed

    # Containers for prepared cells in left, middle and right columns 3 cell columns
    left, middle, right = set(), set(), set()

    x, y = -2, -2
    while x != -1 or y != -1:
        # Prepare the cell in mid_col_x columns and second row
        print("{} {}".format(mid_col_x, 2))

        # Get the judge response
        x, y = tuple(map(int, input().strip().split()))

        # If x == 0 and y == 0, we're done with this test
        if x == 0 and y == 0:
            break

        # Update the corresponding column container
        if x == mid_col_x + 1:
            right.add(y)
        elif x == mid_col_x:
            middle.add(y)
        else:
            left.add(y)

            # If left container has 3 cells, shift the gopher one cell to the right
            if len(left) == 3 and mid_col_x < tot_col_x - 1:
                mid_col_x += 1
                left = middle
                middle = right
                right = set()
    else:
        # The judge returned -1 -1, something went wrong, exiting
        break
