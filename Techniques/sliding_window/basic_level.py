def maxSum(arr: list[int], k: int):
    su = 0
    ma = -1

    for i, x in enumerate(arr):
        su += x

        if i >= k:
            su -= arr[i - k]
        if i >= k - 1:
            ma = max(ma, su)