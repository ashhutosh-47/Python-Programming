# Method-01:-
# def remove_occurrences(nums, target):
#     new_list = []
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] != target:
#             new_list.append(nums[i])
#     return new_list

# nums = [1, 1, 3, 5, 6, 1, 8, 9, 1, 10, 1, 7]
# target = int(input("Enter target = ")) 

# ans = remove_occurrences(nums, target)
# print(ans)


# Method-02:
def remove_occurrences(nums, target):
    while target in nums:
        nums.remove(target)
    return nums
nums = [1, 1, 3, 5, 6, 1, 8, 9, 1, 10, 1, 7]
target = int(input("Enter target = ")) 

ans = remove_occurrences(nums, target)
print(ans)
    