r=int(input("Enter the no. of Rows : "))
c=int(input("Enter the no. of Colums : "))
n=r
row=1
j=0
a=c-2
for i in range(1,n-1):
    if(row==1):
        print("*"*c)
        row=row+1
        j=j+1
    if(2<=row<=n-1):
        print(" "*j+"*"+" "*a+"*")
        row=row+1
        j=j+1
if(row==n):
    print(" "*j+"*"*c)




# row=int(input("Enter the no. of rows : "))
# col=int(input("Enter the no. of columns : "))
# r=1
# i=1
# while(1<=r<=row):
#  if (r==1):
#      print("*"*col)
#      r=r+1
#  elif(1<r<row):
#      print(" "*i + "*" + " "*(col-2)+"*")
#      i=i+1
#      r=r+1
#  elif(r==row):
#      print(" "*i + "*" *col)
#      r=r+1

