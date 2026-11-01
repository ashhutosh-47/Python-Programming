# Method-01:-
# def merge_two_list(nums1, nums2):
#     return nums1 + nums2

# nums1 = [1, 2, 3, 4]
# nums2 = [5, 6, 7, 8, 9, 10]

# ans = merge_two_list(nums1, nums2)
# print(ans)

# Method-02:-
def merge_two_list(nums1, nums2):
    merge_list = []
    for i in nums1:
        merge_list.append(i)
    for i in nums2: 
        merge_list.append(i)
    return merge_list

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8, 9, 10]    
ans = merge_two_list(nums1, nums2)
print(ans)
