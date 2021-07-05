class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])

        res, inter = [], []

        for d in range(n + m - 1):
            inter.clear()
            r, c = 0 if d < m else d - m + 1, d if d < m else m - 1
            



l = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Solution().findDiagonalOrder(l)
