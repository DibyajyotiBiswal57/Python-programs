print("This program will tell you which number is greater")
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

if a>b:
    print(a,"is greater than",b)
elif b>a:
    print(b,"is greater than",a)
else:
    print("Both numbers are equal")