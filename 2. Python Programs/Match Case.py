marks=int(input("Enter Your Marks :- "))
m=marks//10
match m:
    case 10 | 9:
        print("Outstanding")
    case 7 | 8:
        print("Excellent")
    case 6:
        print("Good")
    case 5:
        print("Not Bad")
    case 4:
        print("Pass")
    case m if m<40:
        print("Fail")
    case _:
        print("Invalid Marks")