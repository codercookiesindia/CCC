import sys


n = int(input())
riceBalls = list(map(int, input().split()))
sz = [0] * (n + 1)

for i in range(1, n + 1):
    sz[i] = sz[i - 1] + riceBalls[i - 1]


dp = [[i >= j and (i == j or (j - i <= 2 and riceBalls[i - 1] == riceBalls[j - 1]))
       for j in range(0, n + 1)] for i in range(0, n + 1)]


def calc_three(i, j, sizeIndex):
    for k in range(i + 2, j + 1):
        if dp[k][j]:
            x = sizeIndex.get(sz[j] - sz[k - 1], None)
            if x and x <= k - 2 and dp[x + 1][k - 1]:
                dp[i][j] = True
                yield True
            else:
                yield False


def calc_two(i, j):
    for k in range(i, j):
        if dp[i][k] and dp[k + 1][j] and sz[k] - sz[i - 1] == sz[j] - sz[k]:
            dp[i][j] = True
            yield True
        yield False


def calc(i, j):
    if j > n:
        return 0
    sizeIndex = {sz[k] - sz[i - 1]: k for k in range(i, j - 1) if dp[i][k]}
    dp[i][j] = dp[i][j] or any(calc_three(
        i, j, sizeIndex)) or any(calc_two(i, j))

    if dp[i][j]:
        return sz[j] - sz[i - 1]
    return 0


ans = max([calc(i, i + gap) for gap in range(n)
           for i in range(n + 1)])

print(ans)
