# Method-01
str = input("Enter a string = ")
rev = ""
for ch in str:
    rev = ch + rev    # rev = rev + ch == original str but rev = ch + rev == reverese str becoz of position
if rev == str:
    print(f"String {str} is a Palindrome")
else:
    print(f"String {str} is not a Palindrome")  

# Method-02
# str = input("Enter a string = ")
# rev = ""
# for i in range(len(str)-1, -1, -1):
#     rev += str[i]
# if rev == str:
#     print(f"String {str} is a Palindrome")
# else:
#     print(f"String {str} is not a Palindrome")  