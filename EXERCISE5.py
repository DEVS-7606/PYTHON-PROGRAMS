print("HEALTHY WEALTHY CLINIC")
while(True):
    def getdate():
        import datetime
        return datetime.datetime.now()
    d1={"RETRIVE":1,"LOCK":2}#LOCK FOR LOADING INPUT AND
    # RETRIVE IS FOR ONLY READ DATA
    print("DO you want to LOCK or RETRIVE:")
    D1=input()
    choice1=d1[D1]
    while(choice1==1):
        d2=({"HARRY":"HARRY","ROHAN":"ROHAN","HAMMAD":"HAMMAD"})
        print(d2.keys())
        print("Enter client name:")
        search=str(input())
        d3={"FOOD":1,"EXERCISE":0}
        print("Enter what you want to see FOOD/EXERCISE")
        C=str(input())
        choice2=d3[C]
        while(choice2==1):
            if(search=="HARRY"):
                    f=open("HARRYFOOD.txt")
                    print(f.read())
                    f.close()
            elif(search=="ROHAN"):
                    f = open("ROHANFOOD.txt")
                    print(f.read())
                    f.close()
            elif(search=="HAMMAD"):
                    f = open("HAMMADFOOD.txt")
                    print(f.read())
                    f.close()
            break
        while(choice2==0):
            if (search == "HARRY"):
                    f = open("HARRYEXERCISE.txt")
                    print(f.read())
                    f.close()
            elif (search == "ROHAN"):
                    f = open("ROHANEXERCISE.txt")
                    print(f.read())
                    f.close()
            elif (search == "HAMMAD"):
                    f = open("HAMMADEXERCISE.txt")
                    print(f.read())
                    f.close()
            break
        break
    while (choice1 == 2):
                d2 = ({"HARRY": "HARRY", "ROHAN": "ROHAN", "HAMMAD": "HAMMAD"})
                print(d2.keys())
                print("Enter client name:")
                search = str(input())
                d3 = {"FOOD": 1, "EXERCISE": 0}
                print("Enter what you want to see FOOD/EXERCISE")
                C = str(input())
                choice2 = d3[C]
                while (choice2 == 1):
                    if (search == "HARRY"):
                        f = open("HARRYFOOD.txt","a")
                        p=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + p + "\n"))
                        f.close()
                    elif (search == "ROHAN"):
                        f = open("ROHANFOOD.txt","a")
                        q=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + q + "\n"))
                        f.close()
                    elif (search == "HAMMAD"):
                        f = open("HAMMADFOOD.txt","a")
                        r=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + r + "\n"))
                        f.close()
                    break

                while (choice2 == 0):
                    if (search == "HARRY"):
                        f = open("HARRYEXERCISE.txt","a")
                        x=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + x +"\n"))
                        f.close()
                    elif (search == "ROHAN"):
                        f = open("ROHANEXERCISE.txt","a")
                        y=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + y + "\n"))
                        f.close()
                    elif (search == "HAMMAD"):
                        f = open("HAMMADEXERCISE.txt","a")
                        z=input()
                        print(f.write("[ " + str(getdate()) + " ] : " + z + "\n"))
                        f.close()
                    break
                break
    print("You want surf more again:Y/N")
    check=input()
    if check=="n" or check=="N":
        break

