# Given an m x n matrix mat,
# return an array of all the elements of the array
# in a diagonal order.
class Solution:
    def findDiagonalOrder( mat: list[list[int]]) -> list[int]:
        rowLength = len(mat)
        columnLength = len(mat[0])
        result = []
        intermediary = []
        for diagonal in range(0, rowLength+columnLength-1):
            row = 0 if diagonal < columnLength else diagonal-columnLength+1
            column = diagonal if diagonal < columnLength else columnLength-1
            intermediary.clear()
            while row < rowLength and column >= 0:
                print("row",row,"column",column)
                intermediary.append(mat[row][column])
                row+=1
                column-=1
            if diagonal%2==0:
                for i in range(len(intermediary)-1,-1,-1):
                    result.append(intermediary[i])
            else:
                result.extend(intermediary)
        return result
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution.findDiagonalOrder(mat))
            
