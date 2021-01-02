import sys


def helper(sz):
    if sz == 1:
        return
    overlap = sz * 2 // 3
    if sz % 3 != 0 and sz > 2:
        overlap += 1

    helper(overlap)

    for j in range(n - sz + 1):
        for K in range(j + 1):
            dp[j][K] = max([dp[j][K], dp[j + sz - overlap][K],
                            dp[j + sz - overlap][K + sz - overlap]])


n, k = list(map(int, input().split()))


dp = [list(map(int, input().split())) for i in range(n)]

helper(k)

print(sum(sum(x) for x in dp[:n - k + 1]))
