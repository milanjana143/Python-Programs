a=int(input("Enter number:-"))
s=a
n=0
while a>0 :
    r=a%10
    a=a//10
    n=n*10+r
print(n)  

if n == s :
    print(s,"is a palindrome.")
else :
    print(s,"is not a palindrome.")
    