import sys
from collections import deque

vertices = int(sys.stdin.readline())
adjList = [[int(node) - 1 for node in sys.stdin.readline().split()[1:]]
           for i in range(vertices)]
queue = deque([[0]])
visited = 1
lowest = -1
while queue:
    path = queue.popleft()
    node = path[-1]
    if not adjList[node] and lowest < 0:
        lowest = len(path)
    if lowest > -1 and visited + 1 == 1 << vertices:
        break
    for vertice in adjList[node]:
        if visited >> vertice & 1:
            continue
        visited |= 1 << vertice
        if lowest < 0:
            queue.append(path + [vertice])
        else:
            queue.append([vertice])
print("NY"[visited + 1 == 1 << vertices])
print(lowest)
