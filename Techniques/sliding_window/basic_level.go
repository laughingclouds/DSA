package main

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func maxSum(arr []int, k int) int {
	su, ma := 0, -1

	for i, x := range arr {
		su += x

		if i >= k {
			su -= arr[i-k]
		}

		if i >= k-1 {
			ma = max(ma, su)
		}
	}
	return ma
}
