# Method-01:- In this method original list ele order is not preserved 
# def remove_duplicate(nums):
#     unique_nums = []
#     nums.sort()
#     unique_nums.append(nums[0])
#     for i in range(1, len(nums)):
#         if nums[i-1] != nums[i]:
#             unique_nums.append(nums[i])
#     return unique_nums

# nums = [1, 4, 7, 1, 4, 8, 3, 9, 10]
# ans = remove_duplicate(nums)
# print(ans)

# Method-02:-
def remove_duplicate(nums):
    unique_list = []
    for i in nums:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list   
     
nums = [1, 4, 7, 1, 4, 8, 3, 9, 10]
ans = remove_duplicate(nums)
print(ans)