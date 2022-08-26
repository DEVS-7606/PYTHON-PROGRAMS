b=int(input("Enter the binary number : "))
d=0
i=1
while b!=0:
    r=b%10
    d=d+(r*i)
    i=i*2
    b=int(b/10)
print(f"the decimal no. is {d}")

# print("Enter the Binary Number: ")
# bnum = int(input())
# dnum = 0
# i = 1
# while bnum!=0:
#  rem = bnum%10
#  dnum = dnum + (rem*i)
#  i = i*2
#  bnum = int(bnum/10)
# print("\nEquivalent Decimal Value = ", dnum)
