nums = [[1, 2], [3, 4]]
flips = input()
for flip in flips:
    if flip == 'H':
        nums[0], nums[1] = nums[1], nums[0]
    if flip == 'V':
        nums[0][0], nums[0][1] = nums[0][1], nums[0][0]
        nums[1][0], nums[1][1] = nums[1][1], nums[1][0]

for i in nums:
    for j in i:
        print(j, end='')
        print(' ', end='')
    print('')