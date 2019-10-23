# Solution for - https://open.kattis.com/problems/gears2
__author__ = "Taras Basiuk"

N = int(input().strip()) # read in the number of gears

# Store gear coordinates and radii
gears = []
for i in range(N):
    gears.append(tuple(map(int, input().strip().split()))) # X, Y, R

# Figure out which gears are connected
connected = {}
for i in range(N):
    for j in range(i + 1, N):
        # Check for connection
        if ((gears[i][0] - gears[j][0])**2) + ((gears[i][1] - gears[j][1])**2) != (gears[i][2] + gears[j][2])**2:
            continue

        # Record i gear connection to j gear
        if i in connected:
            connected[i].append(j)
        else:
            connected[i] = [j]

        # Record j gear connection to i gear
        if j in connected:
            connected[j].append(i)
        else:
            connected[j] = [i]

# Helper function for finding greatest common divisor of two positive integers
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

# Rotation ratios of gears relative to the target gear. Target gear rotation ratio is 1/1
ratios = {N - 1: (1, 1)}

# Exploration stack, initialized with target gear (if it's connected to anything)
exploration = []
if N - 1 in connected:
    exploration.append(N - 1)

# While exploration is not done
while exploration:

    old = exploration.pop()
    for new in connected[old]: # iterate through old gear connections

        # Reduced old to new rotation ratio
        rat_num = ratios[old][0] * gears[old][2]
        rat_den = -ratios[old][1] * gears[new][2]
        div = gcd(rat_num, abs(rat_den))
        rat_num = rat_num // div
        rat_den = rat_den // div

        # If the ration is added for the first time add new gear to the exploration queue
        if new not in ratios:
            ratios[new] = (rat_num, rat_den)
            exploration.append(new)
            continue

        # If the new gear was already explored, check that its old rotation ratio is the same
        if ratios[new] != (rat_num, rat_den):
            ratios[0] = -1
            exploration = []
            break

# Output the rotation ratio of the source gear
if 0 not in ratios:
    print(0)
elif ratios[0] == -1:
    print(-1)
else:
    print("{} {}".format(ratios[0][0], ratios[0][1]))
