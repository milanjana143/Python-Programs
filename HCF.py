def hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter The 1st Number :- "))
num2 = int(input("Enter The 2nd Number :- "))
result = hcf(num1,num2)
print("The H.C.F. is =",result)