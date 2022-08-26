# print("ITS AN ARMSTRONG!!!")
# num = int(input("Enter your input :"))
# n = len(str(num))
# d=0
# digit = num
# while digit > 0:
#     a = digit % 10
#     if a>0:
#         b = a ** n
#         d = d + b
#         digit = digit // 10
#     else:
#         a=0
#         d=d+a
#
# if num == d:
#     print("YES!!! your number",num, "is ARMSTRONG")
# else:
#     print("sorry your number",num," is not ARM-STRONG")

################################################################
# num = int(input("Enter a number: "))
# n=len(str(num))
# sum = 0
# temp = num
#
# while temp > 0:
#     digit = temp % 10
#     sum =sum + digit ** n
#     temp=temp // 10
#
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")

#############################################################
print("Write a Python program to check whether the given no is Armstrong or not using user defined function")
def amstrongORnot(num):
    n = len(str(num))
    digit = num
    d = 0
    while digit>0:
        a=digit%10
        b=a**n
        d=d+b
        digit=digit//10
    return d
num = int(input("Enter your input :"))

if num==amstrongORnot(num):
    print("YES!!! your number", num, "is ARMSTRONG")
else:
    print("sorry your number", num, " is not ARM-STRONG")