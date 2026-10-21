num = int(input("Enter number = "))

sum = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum += i
        print(i, end = " ")

print()        
print("Sum of all factors = ", sum)