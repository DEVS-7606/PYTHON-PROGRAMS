n=int(input("Enter the no. of terms:"))
n1=0
n2=1
if(n<0):
    print("Enter positive no.")
elif(n==0):
    print(0)
else:
    while n>0:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        n=n-1