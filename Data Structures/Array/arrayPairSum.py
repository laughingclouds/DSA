class Solution:
    def arrayPairSum(self, arr: list[int]) -> int:
        s, n = 0, len(arr)
        arr.sort()

        for i in range(0, n, 2):
            s += arr[i]
        return s
