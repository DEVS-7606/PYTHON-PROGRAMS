n=int(input("Enter the value of n : "))
m=n
a=0
for row in range(1,n):
        print(" "*a+"*"+" "*((2*m)-1)+"*")
        m=m-1
        a=a+1

else:
        print(" "*(a+1)+"*"+" "*(a+1))

m=m
a=a-1

while(m<=(n-1)):
    print(" "*a+"*"+" "*((2*m)+1)+"*")
    a=a-1
    m=m+1