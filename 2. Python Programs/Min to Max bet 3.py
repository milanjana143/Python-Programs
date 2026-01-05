def largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("The Largest Number is =",num1)
    elif num2>num1 and num2>num3:
        print("The Largest Number is =",num2)
    else:
        print("The Largest Number is =",num3)

num1 = int(input("Enter The 1st Number :- "))
num2 = int(input("Enter The 2nd Number :- "))
num3 = int(input("Enter The 3rd Number :- "))
largest(num1,num2,num3)