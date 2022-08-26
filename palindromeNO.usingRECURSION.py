c=0
def palindrome(n):
    global c
    if n>0:
        b=n%10
        c=(c*10)+b
        palindrome(int(n/10))
    return c

n=int(input("Enter your no. to check here : "))


if palindrome(n)==n:
    print("yes your number is a palindrome no.", n)
else:
    print("No your number is not a palindrome no.", n)