n=int(input("Enter any number :- "))
i=1
f=1
while i<=n:
    f=f+(1/(i*i))
    i+=1
print("Factorial = ",f)