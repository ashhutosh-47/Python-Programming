# Slicing => Slicing is a powerful feature in python that allows you to extract a specific portion or "slice" from a list.It doesn't modify the original list
# instead,it return a new list containing only the selected elements.This is increadibly useful for working with subsets of data efficiently

# Slicing Syntax:-  [start idx : stop idx (Excluded) : step val]

#       0   1   2   3   4   5   6   7   8
# lst = [56, 75, 54, 66, 45, 81, 61, 36, 78]

# list1 = lst[0 : 6]
# print(list1)
# list2 = lst[5 : 8]
# print(list1)
# list3 = lst[0 : 98977]
# print(list3)
# list4 = lst[5 : 5]
# print(list4)
# list5 = lst[4 : ]
# print(list5)
# list6 = lst[ : 5]
# print(list6)
# list7 = lst[0 : 10 : 2]
# print(list7)
# list8 = lst[ : : 3]
# print(list8)

# Step val = +ve  [left -> right]
# Step val = -ve  [right -> left]


#      -9  -8  -7  -6  -5  -4  -3  -2  -1                
#       0   1   2   3   4   5   6   7   8
lst = [56, 75, 54, 66, 45, 81, 61, 36, 78]

list1 = lst[9 : 3]
print(list1) # [] Empty list
list2 = lst[8 : 2 : -1]
print(list2)
list3 = lst[5 : : -1]
print(list3)
list4 = lst[ : : -1]
print(list4) # [78, 36, 61, 81, 45, 66, 54, 75, 56]
list5 = lst[: : -2]
print(list5)
