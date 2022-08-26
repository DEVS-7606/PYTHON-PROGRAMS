x=lambda a,b:a**b
print(x(3,2))

def myfunc(n):
    return lambda a:a**n
mytripler=myfunc(2)
print(mytripler(3))
