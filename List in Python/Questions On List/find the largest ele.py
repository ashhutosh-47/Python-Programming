nums = []
length = int(input("Enter the length of num = "))

for i in range(0, length):
    ele = int(input("Enter the ele = "))
    nums.append(ele)

# Method-01
# largest_ele = max(nums)

# Method-02
largest_ele = float("-inf")  # -ve Infinity
# largest_ele = nums[0]
for i in range(0, length):
    if nums[i] > largest_ele:
        largest_ele = nums[i]
print(largest_ele)
