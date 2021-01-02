import sys
sys.setrecursionlimit(200000)


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


n, m, d = list(map(int, input().split()))
mm = [list(map(int, input().split())) + [x + 1 < n, ] for x in range(m)]
rnk = [1] * (n + 1)
parent = list(range(n + 1))


def main():
    global parent

    mm.sort(key=lambda x: [x[2], not x[3]])
    ee = 0
    dd = 0
    for x in mm:
        if merge(x[0], x[1]):
            ee += 1
            me = x[2]
            if not x[3]:
                dd += 1
            if ee == n - 1:
                if x[3]:
                    return dd
                break
    parent = list(range(n + 1))
    for x in mm:
        if find(x[0]) != find(x[1]):
            if x[2] < me or (x[2] == me and x[3]):
                merge(x[0], x[1])
            elif x[3] and x[2] <= d:
                return dd - 1
    return dd


print(main())
