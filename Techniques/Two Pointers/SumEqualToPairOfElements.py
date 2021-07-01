#  problem statement in the wiki (Techniques--Two pointers)

def isPairSum(arr, n, x):
	i, j = 0, n - 1

	while i < j:
		current_sum = arr[i] + arr[j]
		if current_sum == x:
			return True

		if current_sum < x:
			i += 1
		else:
			j -= 1
	return False


arr = list(map(int, input().split()))
n = len(arr)
x = int(input())
print(isPairSum(arr, n, x))
