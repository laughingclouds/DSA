package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	for i, x := range nums {
		comp := target - x

		if value, flag := m[comp]; flag {
			return []int{value, i}
			// value is actually an index value
		}
		m[x] = i
	}
	return []int{}
}

func alternate(nums []int, target int) []int {
	l := len(nums)
	for i := 0; i < l; i++ {
		for j := i; j < l; j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}
