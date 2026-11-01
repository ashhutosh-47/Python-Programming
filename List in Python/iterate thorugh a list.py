# nums = [10, 20, 25, 30, 40, 45, 50, 55, 100]

# # iterating in a list using WHILE LOOP
# i = 0
# n = len(nums)
# while (i < n):
#     print(nums[i], end = " ")
#     i += 1

# print()

# # iterating in a list using FOR LOOP 
# for i in range(0, n):
#     print(nums[i], end = " ")   

# print ()

# for i in nums:
#     print(i, end = " ")

# Enumerate() function:-
#        0    1   2   3   4   5   6   7   8 
nums = [10, 20, 25, 30, 40, 45, 50, 55, 100]

for idx, val in enumerate(nums):
    print(f"Index = {idx} and Value = {val}")

