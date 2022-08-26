n=int(input("Enter decimal no. : "))
# q=print(bin(n))
d=''
while(n>0):
    c=str(n%2)
    n=n//2
    d=c+d
print(d)

