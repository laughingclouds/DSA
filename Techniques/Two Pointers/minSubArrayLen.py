class Solution:
    def minSubArrayLen(self, arr: list[int], t: int) -> int:
        n = len(arr)
        prefixSumArr = [arr[0]] * n

        for i in range(1, n):
            s = prefixSumArr[i - 1] + arr[i]

            if t <= s:
                return i + 1
            arr[i] = s
        return n + 1

    def returnPrefixSum(self, arr: list[int], t: int) -> int:
        # tuple[int, list[int]]
        n = len(arr)
        sumArr = [arr[0]] * n
        ans = n + 1

        for i in range(1, n):
            sumArr[i] = sumArr[i - 1] + arr[i]
            if t <= sumArr[i]:
                # ans = i + 1
                return i + 1
        # return ans, sumArr


arr = [5, 1, 3, 4, 2]
t = 10
ans = Solution().returnPrefixSum(arr, t)

# i = 0
# for x in array:
#     print(f"index: {i}\tvalue: {x}")
#     i += 1

print(ans)