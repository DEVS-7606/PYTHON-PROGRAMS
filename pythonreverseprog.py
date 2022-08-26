# n=int(input("Enter your input "))
# rev=0
# while(n>0):
#     a=n%10
#     rev=rev*10+a
#     n=n//10
#
# print(rev)

print("----------------------------------")

def reverseNum(num):
    rev_num = 0
    # iterate the loop till num is not equal to zero
    while (num):
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10

    return rev_num

#     # take string input from user
num = int(input('Enter a number: '))

print('Reverse number is: ', reverseNum(num))

