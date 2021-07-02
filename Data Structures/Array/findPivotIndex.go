package main

func pivotIndex(arr []int) int {
	s := 0

	for _, v := range arr {
		s += v
	}

	ans, l, r := -1, 0, s

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
