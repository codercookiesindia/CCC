from bisect import bisect_left, bisect_right
import sys


def find(x):
    if parent[x] != x:

        parent[x] = find(parent[x])
    return parent[x]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if rnk[a] > rnk[b]:
        parent[a] = b
    else:
        parent[b] = a
    if rnk[a] == rnk[b]:
        rnk[b] += 1
    return True


def getTuple():
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    return tuple([c, a, b])


N, M, P, Q = list(map(int, input().split()))
cityEdges = [getTuple() for i in range(P)]
planetEdges = [getTuple() for i in range(Q)]

totalEnergy = sum([e[0] * N for e in cityEdges]) + \
    sum([e[0] * M for e in planetEdges])

cityEdges.sort()
planetEdges.sort()
parent = list(range(M))
rnk = [0] * M

lengths = [e[0] for e in cityEdges if merge(e[1], e[2])]

sums = [0] * M
for i in range(1, M):
    sums[i] = lengths[i - 1] + sums[i - 1]

parent = list(range(N))
rnk = [0] * N

cost = 0
for e in planetEdges:
    if merge(e[1], e[2]):
        i = bisect_left(lengths, e[0], lo=0, hi=M - 1)
        cost += e[0] * (M - i) + sums[i]

cost += sums[M - 1]
print(totalEnergy - cost)
