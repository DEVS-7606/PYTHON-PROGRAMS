n =int(input("Upto how many line ? "))
k = 1
for row in range(1,n+1):
    for column in range(1, row+1):
        print(k,end=" ")
        k = k + 1
    print()