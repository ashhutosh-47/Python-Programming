def squares_of_num(nums):
    square_list = []
    for i in nums:
        num = i*i
        square_list.append(num)
    return square_list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = squares_of_num(nums)
print(ans)    