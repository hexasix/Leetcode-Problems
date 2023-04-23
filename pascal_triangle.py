# Given an integer numRows, 
# return the first numRows of 
# Pascal's triangle.
# In Pascal's triangle, each number 
# is the sum of the two numbers directly 
# above it as shown:
class Solution:
    def generate( numRows: int) -> list[list[int]]:
        result = []
        for row in range(numRows):
            if(row==0):
                result.append([1])
                continue
            if(row==1):
                result.append([1,1])
                continue
            newRow=[0 for i in range(row+1)]        
            #  the nth row has n elements
            for col in range(row+1):
                if(col==0 or col == row):
                    newRow[col]=1
                    continue
                newRow[col] = \
                result[row-1][col-1]+\
                result[row-1][col]
            result.append(newRow)
        return result


print(Solution.generate(5))




        