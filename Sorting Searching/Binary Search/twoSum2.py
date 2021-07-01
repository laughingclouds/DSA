class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        # arr is one-indexed
        n = len(arr)
        for i in range(n):
            l, r = i + 1, n - 1

            t = target - arr[i]

            while r >= l:
                mid = l + (r - l ) // 2

                if arr[mid] == t:
                    return [i + 1, mid + 1]
                elif arr[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
