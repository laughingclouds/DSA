package main

import "sort"

func arrayPairSum(arr []int) int {
	s, n := 0, len(arr)
	sort.Ints(arr)

	for i := 0; i < n; i += 2 {
		s += arr[i]
	}
	return s
}
