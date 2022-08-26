n=int(input("Enter the no.: "))
row=1
j=1
b=n
for i in range(1,n+1):
    a=str(n)
    if(row==1):
        print((a*((n*2)-1)))
        row=row+1
        n=n-1
    elif(row==2,row==n):
        print(a*n+" "*j+a*n)
        n=n-1
        j=j+2
n=2
j=j-4
row=1
while n<=b:
    k=str(n)
    if(2<=n<b):
        print(k*n+" "*j+k*n)
        n=n+1
        j=j-2
    else:
        print(k*((n*2)-1))
        n=n+1

print("-----------------------------------------------------")

# n=int(input("Enter the number: "))
# b=n
# i=1
# row=1
# while n>0:
#  x=str(n)
#  if (row==1):
#      print(x*((n*2)-1))
#      row=row+1
#      n=n-1
#  else:
#      print(x*n+" "*i +x*n)
#      row=row+1
#      n=n-1
#      i=i+2
# n=2
# i=i-4
# row=1
# while n<=b:
#  y=str(n)
#  if 2<=n<b:
#      print(y*n+" "*i +y*n)
#      n=n+1
#      i=i-2
#  else:
#      print(y*((n*2)-1))
#      row=row+1
#      n=n+1

