def duplicateZeros( arr: list[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    # flag=False
    # for index,item in enumerate(arr):
    #     if item==0 and flag==False:
    #         arr.pop()
    #         arr.insert(index,0)
    #         flag=True
    #     elif item!=0 and flag==True:
    #         flag=False
    index=0
    length=(len(arr))
    while index < length:
        if arr[index]==0 and index!= length-1:
            arr.pop()
            arr.insert(index,0)
            index+=1
        index+=1
            


arr=[1,0,2,3,0,4,5,0]
duplicateZeros(arr) #[1,0,0,2,3,0,0,4]

print(arr)


#viable but slow
# class Solution {
#     public void duplicateZeros(int[] arr) {
#         for(int i=0;i<arr.length;i++) {
#         	if(arr[i]==0) {
#         		for(int j=arr.length-1;j>i;j--) {
#         			arr[j]=arr[j-1];
#         		}
#         		i++;
#         	}
#         }
#     }
# }