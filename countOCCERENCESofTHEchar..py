# test_str = "GeeksforGeeks"
test_str=str(input("Enter your sentence or word here : "))
# using naive method to get count
# counting e
count = 0
for i in test_str:#its a for loop not function define
    if i == 'e':
        count = count+1

# printing result
print("Count of "+ i +" in: "+ test_str+" is "
      + str(count))