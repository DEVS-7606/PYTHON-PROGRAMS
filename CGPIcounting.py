n=int(input("Enter no. of subjects:"))
SM=[]
SC=[]
for i in range (1,n+1):
    print("SUBJECT"+str(i))
    sm=int(input("Enter the marks:"))
    sc=int(input("Enter the credit:"))
    SM.append(sm)
    SC.append(sc)
GP=[]
for i in range(0,len(SC)):
    j=i+1
    if (SM[i]>=85and SM[i]<=100):
        print("subject " + str(j) + " Grade = AA")
        gp=10
    elif (SM[i]>=75 and SM[i]<=84):
        print("subject " + str(j) + " Grade = AB")
        gp=9
    elif (SM[i]>=65 and SM[i]<=74):
        print("subject " + str(i) + " Grade = BB")
        gp=8
    elif (SM[i]>=55 and SM[i]<=64):
        print("subject " + str(j) + " Grade = BC")
        gp=7
    elif (SM[i]>=45 and SM[i]<=54):
        print("subject " + str(j) + " Grade = CC")
        gp=6
    elif (SM[i]>=40 and SM[i]<=44):
        print("subject " + str(j) + " Grade = CD")
        gp=5
    elif(SM[i]>=35 and SM[i]<=39):
        print("subject " + str(j) + " Grade = DD")
        gp=4
    else:
        print("subject " + str(j) + " Grade = FF")
        gp=0
    GP.append(gp)

    ci = 0
    for i in range(0, len(SC)):
        ci = ci + SC[i]
    cigi = 0
    for j in range(0, len(GP)):
        cigi = cigi + SC[j] * GP[j]
SPI = cigi/ci
print("SPI = ", SPI)
