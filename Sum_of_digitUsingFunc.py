def sum_of_digit(n):
    b = 0
    c = n
    while (c > 0):
        a = c % 10
        b = b + a
        c = c // 10
        if (b > 9):
            b = sum_of_digit(b)
    return b


x = int(input("Enter the no. here : "))
print("your single value is", sum_of_digit(x))
