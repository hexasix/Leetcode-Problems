def dup_zeros(arr:list[int])->int:
    i=0
    length_arr = len(arr)
    j = length_arr-1
    while i < length_arr:
        if arr[i] == 0:
            while j > i:
                arr[j]=arr[j-1]
                j-=1
            j=length_arr-1
            i+=1
        i+=1
        

arr=[1,0,2,3,0,4,5,0]
dup_zeros(arr) #[1,0,0,2,3,0,0,4]
print(arr)