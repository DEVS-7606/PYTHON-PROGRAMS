n=int(input("Enter the no. of rows : "))
m=n
j=1
for i in range(1,n+1):
    print(" "*(m-1)+"*"*j+" "*(m-1))
    j=j+2
    m=m-1
j=j-4
while(j>0):
    print(" "*(m+1)+"*"*j+" "*(m+1))
    m=m+1
    j=j-2