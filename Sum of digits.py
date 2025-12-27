a=int(input("Enter number:-")) 
n=0
while a!=0 :
    r=a%10
    a=a//10
    n=n+r
print(n) 