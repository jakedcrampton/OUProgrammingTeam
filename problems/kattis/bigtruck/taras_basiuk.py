# Solution for - https://open.kattis.com/problems/bigtruck
__author__ = "Taras Basiuk"

# Read in number of locations, items at locations, and number of roads
n = int(input().strip())
ts = list(map(int, input().strip().split()))
m = int(input().strip())

# Read in the road connectivity between locations graph
graph = {}
for _ in range(m):
    a, b, d = tuple(map(int, input().strip().split()))

    if a - 1 not in graph:
        graph[a - 1] = {}

    if b - 1 not in graph:
        graph[b - 1] = {}

    graph[a - 1][b - 1] = d
    graph[b - 1][a - 1] = d

# Keep track of shortest dist from source, and max items collected
visited = [None] * n
visited[0] = (0, ts[0])

# Prepare exploration queue and exploration plan
from collections import deque
exploration = deque()
exploration.append(0)

exploration_plan = set()
exploration_plan.add(0)

while exploration:
    # Get the current location
    loc = exploration.popleft()
    exploration_plan.remove(loc)

    if loc not in graph: # Source location might not have roads anywhere
        continue

    # For each possible destination from current location
    for dest in graph[loc]:
        # Check how quickly ww will get there from here, and how many items we will bring
        candidate = (visited[loc][0] + graph[loc][dest], visited[loc][1] + ts[dest])

        # If we visit destination for the first time, can get there faster, or bring more items
        if not visited[dest] or candidate[0] < visited[dest][0] or (candidate[0] == visited[dest][0] and candidate[1] > visited[dest][1]):
            visited[dest] = candidate # Update the shortest distance or max items brought

            # If we don't already plan to explore from the destination, update exploration queue and plan
            if dest not in exploration_plan:
                exploration.append(dest)
                exploration_plan.add(dest)

# Report the result
print("impossible" if not visited[n - 1] else "{} {}".format(visited[n - 1][0], visited[n - 1][1]))
