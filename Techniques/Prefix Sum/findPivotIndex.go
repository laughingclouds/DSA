package main

func pivotIndex(arr []int) int {
	r := 0

	for _, v := range arr {
		r += v
	}

	ans, l := -1, 0

	for i, v := range arr {
		r -= v
		if l == r {
			ans = i
			break
		}
		l += v
	}
	return ans
}
