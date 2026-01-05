n=int(input("Enter Any Number :- "))
p=n
s=0
while n>0:
    r=n%10
    s=((s*10)+r)
    n=n//10
if s==p:
    print(p,"is a Palindrome Number.")
else:
    print(p,"is not a Palindrome Number.")