def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("Enter your number : "))
print("for number",number,"fibonacci number is ",fibonacci(number))