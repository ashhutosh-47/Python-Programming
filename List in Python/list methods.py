# lst = ["Deva", 20, 21.61, True, "Delhi"]
# #        0     1     2      3      4

# print(lst, id(lst))

# # append method:-
# # lst.append("Kolkata")
# # lst.append("hello")
# # lst.append(54)
# # print(lst)

# # insert method:-
# lst.insert(2, "Chennai")
# lst.insert(5, 7)
# lst.insert(0, "Ashutosh")
# print(lst, id(lst))

# # pop method:- DELETE ELEMENT BY INDEX
# pop_val = lst.pop() # pop at the last idx value
# lst.pop(0) # pop at the any idx value
# print(pop_val)
# print(lst, id(lst))

# # remove method:- DELETE ELEMENT BY VALUE
# lst.remove(True)
# lst.remove("Deva")
# print(lst, id(lst))

#       0  1  2  3  4  5   6  7  8  9 10  11 12 13
nums = [1, 6, 7, 4, 8, 9, 10, 1, 2, 4, 1, 5, 1, 7]

# sort vs sorted:-
new_list = sorted(nums) # Sorted function gives you a new list

# print(f"New list = {new_list}, Id = {id(new_list)}")
# print(f"Old list = {nums}, Id = {id(nums)}")


# print(f"list = {nums}, Id = {id(nums)}")
# nums.sort() # sort is a method which sort the list internally (In-Place sorting)
# print(f"list = {nums}, Id = {id(nums)}")
# nums.sort(reverse = True)
# print(f"list = {nums}, Id = {id(nums)}")

# reverse method:-
# print(f"List before reversed = {nums}, Id = {id(nums)}")
# nums.reverse()
# print(f"List after reversed = {nums}, Id = {id(nums)}")

# index method:- Which gives you Element index
nums_ele_idx = nums.index(10) 
print(nums_ele_idx)

# count method:-
nums_ele_count = nums.count(1)
print(nums_ele_count)