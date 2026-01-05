str1 = input("Enter The 1st String :- ")
str2 = input("Enter The 2nd String :- ")
if len(str1)!=len(str2):
    print("Both String's are not Anagram.")
else:
    if sorted(str1)==sorted(str2):
        print("Both String's are Anagram")
    else:
        print("Both String's are not Anagram.")