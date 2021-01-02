N = input()
swifts = input().split()
semaphores = input().split()
sf = 0
se = 0
last = 0
for i in range(int(N)):
    sf += int(swifts[i])
    se += int(semaphores[i])
    if se == sf:
        last = i+1
print(last)
