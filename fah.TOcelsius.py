def fahTOcel(f):
    return (f-32)*(5/9)
fah=float(input("Enter your temperature in fahrenheit in here :"))
cel=fahTOcel(fah)
print(cel)