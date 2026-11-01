# Method-01:-
# def reverse_list(nums):
#     n = len(nums)
#     reverse = []
#     for i in range(n-1, -1, -1):
#         reverse.append(nums[i])
#     return reverse

# nums = []
# length = int(input("Enter the length of num = "))

# for i in range(0, length):
#     ele = int(input("Enter the ele = "))
#     nums.append(ele)

# ans = reverse_list(nums)
# print(ans)

# Method-02:-
def reverse_list(nums):
    n = len(nums)
    i = 0
    j = n-1
    while(i <= j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1
    return nums    

nums = []
length = int(input("Enter the length of num = "))

for i in range(0, length):
    ele = int(input("Enter the ele = "))
    nums.append(ele)

ans = reverse_list(nums)
print(ans)