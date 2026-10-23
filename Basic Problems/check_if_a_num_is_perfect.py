# Definition of a Perfect Number-
# A perfect number is a positive integer that is equal to the sum of its positive divisors excluding itself.

# Example:- num = 6   divisors -> 1,2,3,6
# sum = 1 + 2 + 3 = num so 6 is a perfect number.

num = int(input("Enter number = "))

sum_divisors = 0
for i in range(1, num + 1):
    if num % i == 0 and i != num:
        sum_divisors += i

if sum_divisors == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")
