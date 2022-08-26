n=int(input("Enter the no. of lines: "))
row=1
for i in range(1,n+1):
    if(row==1):
        print("*"*n*2)
        n=n-1
        row=row+1
    else:
        print("*"*n+" "*i+"*"*n)
        n=n-1
        i=i+1
