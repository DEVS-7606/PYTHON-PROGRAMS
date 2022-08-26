a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
if(a>=0 and b>=0):
    if(a<=b):
        for i in range(a,b+1):
            if(i==1):
                print("one")
            elif(i==2):
                print("two")
            elif(i==3):
                print("three")
            elif(i==4):
                print("four")
            elif(i==5):
                print("five")
            elif(i==6):
                print("six")
            elif(i==7):
                print("seven")
            elif(i==8):
                print("eight")
            elif(i==9):
                print("nine")
            else:
                if(i%2==0):
                    print("even")
                else:
                    print("odd")
    else:
        print("a is more than b")
else:
    print("a positive dal na samaj nai padta loudeya")