def replace_neg_num(nums):
    n = len(nums)
    for i in range(0, n):
        if nums[i] < 0:
            nums[i] = 0
    return nums

nums = [1, 2, 14, -10, 1, -4, 9, -6, -3]
ans = replace_neg_num(nums)
print(ans)