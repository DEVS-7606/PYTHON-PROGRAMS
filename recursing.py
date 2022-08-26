def factorial_recursive(n):
    if n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)
number=int(input("Enter the no. here : "))
print("the factorial using recursive method",factorial_recursive(number))
##########################################################
"""THis function only tales zero and positive no."""
def factorial_recursive(n):
    if(n>=0):
        if n==0:
            return 1
        else:
            return n*factorial_recursive(n-1)
number=int(input("Enter the no. here : "))
print("the factorial using recursive method",factorial_recursive(number))