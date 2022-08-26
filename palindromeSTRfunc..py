# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s =str(input("Enter your spelling here to check :"))
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")
# def ISPALINDROME(s):
#     return s==s[::-1]
# s=str(input("Enter name here:"))
# s=ISPALINDROME(s)
#
# if s:
#     print("yes")
# else:
#     print("no")
def is_palindrome(s):
    if s==s[::-1]:
        return print("Yes")
    else:
        return print("no")
name=str(input("Enter the name here:\n"))
name=is_palindrome(name)