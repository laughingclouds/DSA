class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        # arr is one-indexed
        l, r = 0, len(arr) - 1

        while r > l:
            s = arr[l] + arr[r]

            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return []