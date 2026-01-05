def BSA (arr,SE):
    left = 0
    right = len(arr)-1
    while(left<=right):
        mid = left+(right-left)//2
        if arr[mid]==SE:
            return mid
        elif arr[mid]>SE:
            right = mid-1
        else:
            left = mid+1
    return -1
arr = []
i=0
n = int(input("Enter The Range of Array :- "))
print("Enter Array Elements :- ")
for i in range(0,n):
    element = int(input())
    arr.append(element)
SE = int(input("Enter Searching Element :- "))
result = BSA (arr,SE)
if result!=-1:
    print("Search is Successful.")
else:
    print("Search is Unsuccessful.")