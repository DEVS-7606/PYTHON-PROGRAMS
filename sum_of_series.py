n=int(input("number of terms: "))
a=int(input(("Enter the digit: ")))
b=a
d=0
while(n>1):
    print(b,end='+')
    d=b+d
    c=(b*10)
    b=c+a
    n=n-1
else:
    print(b)
    d=b+d
    print("Sum of above series is: ",d)