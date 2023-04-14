def checkIfExist( arr: list[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == 2*arr[j] and i!=j:
                print("i=",i,"j=",j)
                return True
    return False        



arr=[-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))