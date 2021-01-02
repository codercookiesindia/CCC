
import sys
MAXN = 1000002


def update(i, v):
    i = MAXN - i - 1
    while i < MAXN:
        if BIT[i] < v:
            BIT[i] = v
        i += i & -i


def suffixMax(i):
    ret = 0
    i = MAXN - i - 1
    while i > 0:
        if ret < BIT[i]:
            ret = BIT[i]
        i -= i & -i
    return ret


N, K = list(map(int, input().split()))
MAXN = (N + 2)
BIT = [0] * MAXN
mxDp = [0] * MAXN


A = [0, ] + list(map(int, input().split()))

dp = [0] * MAXN
mn = [0] * MAXN
mxA = [0] * MAXN

curDay = 1
curBack = 0
mxA3 = 0
for i in range(1, N + 1):

    if mxA3 < A[i]:
        mxA3 = A[i]
    v = max([mn[curDay - 1], i - K])
    while v <= curBack and mxA[curBack] <= A[i]:
        update(curBack, mxDp[curBack] + A[i])
        mxA[curBack] = A[i]

        if v <= curBack - 1 and mxA[curBack - 1] <= A[i]:
            curBack -= 1
        else:
            break
    while curBack < v:
        update(curBack + 1, mxDp[curBack + 1] + mxA3)
        mxA[curBack + 1] = mxA3
        curBack += 1
    dp[i] = suffixMax(v)

    if i % K == 0:
        j = i
        mxA2 = 0
        while j >= mn[curDay]:
            update(j, dp[j] + mxA2)
            mxA[j] = mxA2
            if mxA2 < A[j]:
                mxA2 = A[j]
            mxDp[j] = max([mxDp[j + 1], dp[j]])
            j -= 1
        curDay += 1
        mn[curDay] = i + 1
        curBack = i
        mxA3 = 0

print(dp[N])
