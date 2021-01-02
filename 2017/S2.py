
N = int(input())
d = list(map(int, input().split()))

if N % 2 == 0:
    d.sort()
    lo = d[0:(N//2)]
    lo.reverse()
    high = d[(N//2):N]

    for i in range(N//2):
        print(lo[i], end=' ')
        print(high[i], end=' ')
    print('')
else:
    d.sort()
    lo = d[0:((N//2)+1)]
    lo.reverse()
    high = d[((N//2)+1):N]
    for i in range(N//2):
        print(lo[i], end=' ')
        print(high[i], end=' ')
    print(lo[(N//2)])
