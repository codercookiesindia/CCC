def main():
    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    if t != 1:
        b.sort(reverse=True)
    else:
        b.sort()
    s = 0
    for x in range(n):
        s += max([a[x], b[x]])
    print(s)


main()
