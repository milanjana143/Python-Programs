a=1
while a<=100:
    if a%3==0 or a%5==0:
        if a%3==0 and a%5==0:
            print(a,"Fizz Buzz")
        elif a%5==0:
             print(a,"Buzz")
        else:
            print(a,"Fizz")
    else:
        print(a)
    a+=1