def is_target_exist(nums, target):
    for i in range(0, length):
        if nums[i] == target:
            return True
    return False    

nums = []
length = int(input("Enter the length of num = "))
for i in range(0, length):
    ele = int(input("Enter the ele = "))
    nums.append(ele)
target = int(input("Enter the target = "))

ans = is_target_exist(nums,target)
print(ans)
