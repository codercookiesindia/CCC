
N = int(input())
memo = {}


def f(n):
    if n == 1:
        return 1
    if n not in memo:
        total = n - (n >> 1)
        kth = 2
        while True:
            partition = n // kth
            if partition ** 2 > n:
                total += f(kth) * (partition - n // (kth + 1)) + f(partition)
            elif kth == partition:
                total += f(kth) * (partition - n // (kth + 1))
            else:
                break
            kth += 1
        memo[n] = total
    return memo[n]


print(f(N))
