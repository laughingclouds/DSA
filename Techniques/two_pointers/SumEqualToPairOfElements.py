def isPairSum(arr, n, x):
	i, j = 0, n - 1

	max_sum_pairs = f"{arr[0]} {arr[n - 1]}"
	diff = x

	while i < j:
		current_sum = arr[i] + arr[j]
		if abs(current_sum - x) <= diff:
			max_sum_pairs = f"{arr[i]} {arr[j]}"
			diff = abs(current_sum - x)
		
		if current_sum < x:
			i += 1
		else:
			j -= 1

	return max_sum_pairs


arr = list(map(int, input().split()))
n = len(arr)
x = int(input())
print(isPairSum(arr, n, x))
