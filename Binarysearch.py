def BinarySearch(listD, key):
    low = 0
    high = len(listD) - 1
    Found = False
    while low<=high and not Found:
        mid = (low+high)//2
        if key == listD[mid]:
            Found = True
        elif key>listD[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("The key has been Found")
    else:
        print("Key hasn't been Found")
listD = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
print(listD)
key = int(input("Enter the key: "))
BinarySearch(listD, key)