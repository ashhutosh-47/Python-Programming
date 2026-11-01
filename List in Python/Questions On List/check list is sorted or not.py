def is_sorted(nums):
    n = len(nums)
    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            return False
    return True        

nums = []
length = int(input("Enter the length of num = "))

for i in range(0, length):
    ele = int(input("Enter the ele = "))
    nums.append(ele)

ans = is_sorted(nums)
print(ans)