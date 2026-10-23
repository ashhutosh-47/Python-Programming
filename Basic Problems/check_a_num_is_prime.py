# Definition of a Prime Number:
# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and the number itself.

# Example:- 7, 23, 11.....

num = int(input("Enter number = "))

cnt = 0
for i in range(1,num + 1):
    if num % i == 0:
        cnt += 1

if cnt == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")        