class Solution:
    def dominantIndex(self, arr: list[int]) -> int:
        m = max(arr)
        maxIndex = arr.index(m)

        for i, v in enumerate(arr):
            if m != v and m < 2 * v:
                maxIndex = -1
                break
        return maxIndex
        