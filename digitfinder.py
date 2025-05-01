print("This program tells if a number has 1,2 or more digits.")
num=int(input("Enter a number: "))
if num<0 or num>0:
    absnum=abs(num)
if absnum>=0 and absnum<=9:
    print(f"{num} has only one digit.")
elif absnum>=10 and absnum<=99:
    print(f"{num} has two digits.")
else:
    print(f"{num} has more than 2 digits.")
