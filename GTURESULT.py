n=int(input("Enter no. of subjects:"))
d=1
SM=[]
SC=[]
GP=[]
a=0
b=0
CiGi=[]
while(d<=n):
        print("subject",d,":")
        sm=int(input("Enter the marks scored in exam : "))
        sc=int(input("Enter the credits of subject : "))
        d=d+1
        SM.append(sm)
        SC.append(sc)
for i in range(0,len(SM)):
    print("Subject",i+1, ":")
    if (85 <= SM[i] <= 100):
                print("Grade is AA")
                print("Grade point is 10")
                gp=10
    elif (75 <= SM[i] <= 84):
                print("Grade is AB")
                print("Grade point is 09")
                gp=9
    elif (65 <= SM[i]<= 74):
                print("Grade is BB")
                print("Grade point is 08")
                gp=8
    elif (55 <= SM[i] <= 64):
                print("Grade is BC")
                print("Grade point is 07")
                gp=7
    elif (45 <= SM[i] <= 54):
                print("Grade is CC")
                print("Grade point is 06")
                gp=6

    elif (40 <= SM[i] <= 44):
                print("Grade is CD")
                print("Grade point is 05")
                gp=5

    elif (35 <=SM[i]<= 39):
                print("Grade is DD")
                print("Grade point is 04")
                gp=4

    else:
                print("Grade is FF")
                print("Grade point is 00")
                gp=00
    GP.append(gp)
for i in range(0,len(SM)):
    CiGi.append(SC[i]*GP[i])
    b=b+CiGi[i]
    a=a+SC[i]

SPI = b / a
print("Total SPI : ",SPI)