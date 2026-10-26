# # Method-01:-
# num = int(input("Enter a number = "))
# temp = num
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev*10 + rem
#     num //= 10

# if rev == temp:
#     print(f"{temp} is a Palindrome")
# else:
#     print(f"{temp} is not a Palindrome")

# Method-02:-
num = int(input("Enter a number = "))
temp = num

if (num < 0) or (num % 10 == 0 and num != 0): 
    print(f"{temp} is not a Palindrome")
    
else:
    rev = 0
    while num > rev:
            rem = num % 10
            rev = rev*10 + rem
            num //= 10
    
    if (rev == num) or (rev // 10 == num):
            print(f"{temp} is a Palindrome")
    else:
            print(f"{temp} is not a Palindrome")    

