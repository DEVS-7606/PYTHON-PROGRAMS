n=int(input("Enter the no.:"))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("the new no. formed:",d)
