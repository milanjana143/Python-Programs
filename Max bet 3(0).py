a = int(input("Enter 1st Number "))
b = int(input("Enter 2nd Number "))
c = int(input("Enter 3rd Number "))

if a>b and a>c:
    print(a," is large number.")
elif b>a and b>c :
    print(b," is large number.")
else:
    print(c," is large number.")