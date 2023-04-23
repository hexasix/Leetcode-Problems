class Solution:
    def spiralOrder(matrix: list[list[int]]) -> list[int]:
        rowLength = len(matrix)
        colLength = len(matrix[0])
        total = rowLength*colLength
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        visited = [False for i in range(total)]
        result = []
        row, col = 0, 0  # index
        for i in range(total):
            result.append(matrix[row][col])
            visited[colLength*(row)+(col)] = True
            nextRow = row+directions[directionIndex][0]
            nextCol = col + directions[directionIndex][1]
            isDirectionChange = \
                not (0 <= nextRow < rowLength
                     and 0 <= nextCol < colLength and not visited[colLength*(nextRow)+(nextCol)])
            if (isDirectionChange):
                directionIndex = (directionIndex+1) % 4
            row = row+directions[directionIndex][0]
            col = col + directions[directionIndex][1]

        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution.spiralOrder(matrix))
