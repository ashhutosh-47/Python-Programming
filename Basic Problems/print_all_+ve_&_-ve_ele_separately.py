# # Method-01:-
# list = []
# len_list = int(input("Enter length of a list = "))

# for i in range(len_list):
#     list_ele = int(input("Enter list ele = "))
#     list.append(list_ele)

# pos_ele = []
# neg_ele = []

# for i in range(len(list)):
#     if list[i] >= 0:
#         pos_ele.append(list[i])
#     else:
#         neg_ele.append(list[i])

# print ("Postive element:")
# for i in pos_ele:
#     print(i, end = " ")

# print ()
# print ("Negative element:")
# for i in neg_ele:
#    print(i, end = " ")        

# Method-02:-
list = []
len_list = int(input("Enter length of a list = "))

for i in range(len_list):
    list_ele = int(input("Enter list ele = "))
    list.append(list_ele) 

for i in range(len(list)):
    if list[i] > 0:
        print(list[i], end = " ")  
    else:
        print(list[i], end = " ")    
