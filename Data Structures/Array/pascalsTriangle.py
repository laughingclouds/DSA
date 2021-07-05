class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1: return [[1] * numRows]
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle

print(Solution().generate(2))