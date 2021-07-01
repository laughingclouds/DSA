package main

func twoSum2(nums []int, target int) []int {
	// array is one-indexed
	l, r := 0, len(nums)-1

	for r > l {
		s := nums[l] + nums[r]

		if s == target {
			return []int{l + 1, r + 1}
		}

		if s < target {
			l++
		} else {
			r--
		}
	}
	return []int{}
}
