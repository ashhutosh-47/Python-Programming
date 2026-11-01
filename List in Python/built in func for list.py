marks = [45, 7, 18, 61, 54, 81]

# Length 
n = len(marks)
print(f"Length of list = {n}")

# Maximum element
maxi = max(marks)
print(f"Maximum marks = {maxi}")

# Minimum element
mini = min(marks)
print(f"Minimum marks = {mini}")

# Total marks 
total = sum(marks)
print(f"Total marks = {total}")

# To sort using sorted(), it will always return you a new list and in ascending order
sorted_marks = sorted(marks)
print(f"Sorted marks = {sorted_marks}")
print(f"Unsorted marks = {marks}")

# desecnding order
sorted_marks = sorted(marks, reverse = True)
print(f"Sorted marks = {sorted_marks}")
print(f"Unsorted marks = {marks}") 


