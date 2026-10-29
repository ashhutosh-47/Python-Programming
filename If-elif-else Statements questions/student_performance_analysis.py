# Q1. Student Performance Analysis (K3)
# A college maintains marks in five subjects. Write a Python program to:
# (i) accept the five marks and calculate total and percentage;
# (ii) display PASS only when percentage ≥40 and every subject mark ≥33, otherwise FAIL;
# (iii) assign grade A (≥80), B (≥60), C (≥40), or D (<40) according to percentage.

marks = []
number_of_subject = int(input("Enter number of subject = "))

for i in range(number_of_subject):
    Subject_marks = int(input("Enter marks = "))
    marks.append(Subject_marks)

total = 0
for i in marks:
    total += i
    if i >= 33:
        is_pass = True
    else:
        is_pass = False
        break
percentage = total / len(marks)
if is_pass and percentage >= 40:
    print("PASS")
else:
    print("FAIL")
print("Marks = ", marks)
print("Total = ", total)
print("Percentage = ", percentage)

if percentage >= 80:
    print("Grade = A")
elif percentage >= 60:
    print("Grade = B")
elif percentage >= 40:
    print("Grade = C")
else:
    print("Grade = D")
