v = sorted(int(input()) for index in range(int(input())))
ret = float("Inf")
for index in range(2, len(v)):
    ret = min(ret, (v[index] - v[index - 2]) / 2)
print("%.1f" % ret)
