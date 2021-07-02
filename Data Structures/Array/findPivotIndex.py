class Solution:
    def pivotIndex(self, arr: list[int]) -> int:
        ans, l, r = -1, 0, sum(arr)

        for i, v in enumerate(arr):
            r -= v
            if l == r:
                ans = i
                break
            l += v
        return ans
        