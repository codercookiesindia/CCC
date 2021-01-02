from random import randint
import sys


def fill(grid):
    for _ in range(9):
        for side in range(2):
            for pos, (i, j, k) in enumerate(grid):
                if j == "X" and i != "X" != k:
                    j = i + k >> 1
                elif k == "X" and i != "X" != j:
                    k = j + j - i
                elif i == "X" and j != "X" != k:
                    i = j + j - k
                grid[pos] = [i, j, k]
            grid = list(map(list, zip(*grid)))

    if any([i + k != j + j for table in (grid, zip(*grid)) for i, j, k in table if X not in (i, j, k)]):
        return 0

    return grid


def helper(state):

    state = fill(state[:])

    if state == 0:  # Invalid
        return 0

    if all([i != "X" for row in state for i in row]):
        return state

    for row in range(3):
        if "X" in state[row]:
            col = state[row].index("X")
            for _ in range(5):
                # Fill a random
                state[row][col] = randint(-1000000, 1000000)
                value = helper(state[:])
                if value:
                    return value
            state[row][col] = X


X = "X"
result = helper([map(eval, input().split()) for i in range(3)])
for i, j, k in result:
    print(i, j, k)
