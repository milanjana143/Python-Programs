def fact(num):
    if num == 0 or num == 1:  # Base case
        return 1
    return num * fact(num - 1)

num = int(input("Enter Any Number :- "))
result = fact(num)
print("The Factorial of",num,"is =",result)