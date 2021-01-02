from math import sqrt


def eval(i):

    l = L[i]
    idx = (ind[i] + cur[l]) % L_lines[l]
    return A[lines[l][idx]]


def val(s, e):
    for i in range(s, e + 1):
        yield eval(i)


n, m, Q = list(map(int, input().split()))
SIZE = 400
NBLOCK = n // SIZE + 1
RHT = [[-1] * NBLOCK for i in range(m + 1)]
L = [0, ] + list(map(int, input().split()))
assert len(L) == n + 1
lines = [[] for i in range(m + 1)]
ind = [0] * (n + 1)
for i, l in enumerate(L):
    if i > 0:
        assert l <= m and l > 0
        lines[l].append(i)
        ind[i] = len(lines[l]) - 1
        RHT[l][i // SIZE] = i

L_lines = [len(lines[i]) for i in range(len(lines))]
A = [0, ] + list(map(int, input().split()))
assert len(A) == n + 1
SQRT = [0] * NBLOCK
for i, a in enumerate(A):
    if i > 0:
        SQRT[i // SIZE] += a

cur = [0] * (m + 1)
for q in range(Q):
    s = list(map(int, input().split()))

    if s[0] == 1:
        assert len(s) == 3
        l, r = s[1:]
        assert l <= n and r <= n and l <= r and l > 0 and r > 0
        ans = 0
        p = ((l + SIZE - 1) // SIZE)
        q = r // SIZE
        if p >= q:
            ans = sum(val(l, r))
        else:
            ans += sum(val(l, p * SIZE - 1))
            ans += sum(SQRT[p: q])
            ans += sum(val(q * SIZE, r))
        print(ans)
    else:
        assert len(s) == 2
        x = s[1]
        assert x <= m and x > 0
        start = -1
        prev = 0
        for i, rt in enumerate(RHT[x]):
            if rt == -1:
                continue
            if start == -1:
                start = i
            SQRT[i] += prev
            prev = eval(rt)
            SQRT[i] -= prev
        SQRT[start] += prev
        cur[x] -= 1
        if cur[x] < 0:
            cur[x] += L_lines[x]
