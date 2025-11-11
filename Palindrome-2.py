def palindrome(num):
    p=num
    s=0
    while num>0:
        r=num%10
        s=((s*10)+r)
        num=num//10
    if s==p:
        print(p,"is a Palindrome Number.")
    else:
        print(p,"is not a Palindrome Number.")

num=int(input("Enter Any Number :- "))
palindrome(num)