n=int(input("Enter Any Number :- "))
d=n
m=n
c=0
a=0
while d>0:
    d=d//10
    c+=1
for i in range(0,c,1):
    r=m%10
    a=a+r**c
    m=m//10
if n==a:
    print(n,"is a Armstrong Number.")
else:
    print(n,"is not a Armstrong Number.")