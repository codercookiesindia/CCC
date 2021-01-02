from math import log2
import sys


n, t = input().split()
n = int(n)
t = int(t)
s = input().strip()
oG = [ord(x) - ord('0') for x in s]
nG = [0] * n
for p in range(50, -1, -1):
    if ((2 ** p) & t) > 0:
        lp = 2 ** p
        for x in range(n):
            q = (x - lp) % n
            nG[x] = oG[q + (n if q < 0 else 0)] ^ oG[(x + lp) % n]
        oG, nG = nG, oG
print("".join(map(str, oG)))
