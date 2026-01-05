def leapyear(year):
    if year%400==0:
        print(year,"is Leap Year.")
    elif year%100==0:
        print(year,"is Leap Year.")
    elif year%4==0:
        print(year,"is Leap Year.")
    else:
        print(year,"is not Leap Year.")

year = int(input("Enter Any Year :- "))
leapyear(year)