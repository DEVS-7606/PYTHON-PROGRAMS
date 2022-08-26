n=int(input("Enter the value of n: "))
i=1
row=1
b=n
while 1<=row<=n:
    if(row<3 or row==n):
        print("* "*n)
        row=row+1

    else:
        print("* "+"  "*i+"* "*(b-2))
        i=i+1
        b=b-1
        row=row+1