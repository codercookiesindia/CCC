grid = [[*map(int, input().split())] for i in range(int(input()))]

lowest = min(map(min, grid))

while lowest != grid[0][0]:
    grid = [*zip(*grid[::-1])]

for i in grid:
    print(" ".join(map(str, i)))
